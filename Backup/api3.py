from flask import Flask
from flask import request,Response, jsonify, make_response
import json
import re
from flask_cors import CORS
from unidecode import unidecode
from buscaApelidos import getApelidos
from clinicalTrials.getapi import todos_hospitais
from datetime import datetime
app = Flask(__name__)
CORS(app)


def convert_month_year_to_dd_mm_yyyy(date_str):
    # Mapeamento de nomes de meses para números
    month_mapping = {
        'January': '01',
        'February': '02',
        'March': '03',
        'April': '04',
        'May': '05',
        'June': '06',
        'July': '07',
        'August': '08',
        'September': '09',
        'October': '10',
        'November': '11',
        'December': '12'
    }
    data_formatada = ''
    lista_de_strings = date_str.split(' ')
    if len(lista_de_strings) == 3:
        month = month_mapping[lista_de_strings[0]]
        day = lista_de_strings[1].replace(',', '')
        year = lista_de_strings[2]
        data_formatada = f'{"0" + day if len(day) == 1 else day }-{month}-{year}'
    else:
        if len(lista_de_strings) == 2:
            month = month_mapping[lista_de_strings[0]]
            year = lista_de_strings[1]
            data_formatada = f'01-{month}-{year}'
        else:
            return None
    return data_formatada



def validaDatas(datainicial):
    try:
        data = datainicial.split('-')
        if len(data) != 3:
            return make_response(jsonify({"status":"Data inválida"})), 200
        if len(data[0]) != 2 or len(data[1]) != 2 or len(data[2]) != 4:
            return make_response(jsonify({"status":"Data inválida"})), 200
        if int(data[0]) > 31 or int(data[0]) < 1:
            return make_response(jsonify({"status":"Data inválida"})), 200
        if int(data[1]) > 12 or int(data[1]) < 1:
            return make_response(jsonify({"status":"Data inválida"})), 200
    except:
        return make_response(jsonify({"status":"Data inválida"})), 200
    
    return True

@app.route('/estudos', methods=['GET'])
def estudos():
    datainicial = ''
    if request.args.get('datainicial') is not None:
        datainicial = request.args['datainicial']
    
    dados = {}
    hospitais = todos_hospitais()
    if datainicial:
        if validaDatas(datainicial) != True:
            return validaDatas(datainicial)
        datainicial = datetime.strptime(datainicial, '%d-%m-%Y').date()
        for estudo in hospitais:    
                try:
                    dataEstudo = convert_month_year_to_dd_mm_yyyy(estudo['StartDate'][0])
                    dataEstudo = datetime.strptime(dataEstudo, '%d-%m-%Y').date()
                    if dataEstudo  >= datainicial:
                        LocationFacility = estudo['LocationFacility']
                        LeadSponsorName = estudo['LeadSponsorName']
                        hospitais_na_base = open('hospitais.json', 'r').read()
                        hospitais_na_base = json.loads(hospitais_na_base)['hospitais']
                        if len(LeadSponsorName) > 0:
                            fharma = LeadSponsorName[0]
                            for hospital in LocationFacility:
                                foi = False
                                for apelido in hospitais_na_base.items():
                                        if hospital in apelido[1]:
                                            hospital = apelido[0]
                                            foi = True
                                            break
                                if fharma in dados:
                                    if foi:
                                        if hospital not in dados[fharma]:
                                            dados[fharma][hospital] = 1
                                        else:
                                            dados[fharma][hospital] += 1
                                else:
                                    dados[fharma] = {}
                                    if foi:
                                        dados[fharma][hospital] = 1
                    else:
                        continue
                except:
                    continue
            
    else:
        for estudo in hospitais:
            LocationFacility = estudo['LocationFacility']
            LeadSponsorName = estudo['LeadSponsorName']
            hospitais_na_base = open('hospitais.json', 'r').read()
            hospitais_na_base = json.loads(hospitais_na_base)['hospitais']
            if len(LeadSponsorName) > 0:
                fharma = LeadSponsorName[0]
                for hospital in LocationFacility:
                    foi = False
                    for apelido in hospitais_na_base.items():
                            if hospital in apelido[1]:
                                print(apelido[0])
                                hospital = apelido[0]
                                foi = True
                                break
                    if fharma in dados:
                    
                        if foi:
                            if hospital not in dados[fharma]:
                                dados[fharma][hospital] = 1
                            else:
                                dados[fharma][hospital] += 1
                    else:
                        dados[fharma] = {}
                        if foi:
                            dados[fharma][hospital] = 1
    dados_formatados = {}
    for fharma in dados:
        if dados[fharma] != {}:
            dados_formatados[fharma] = dados[fharma]

        
    return make_response(jsonify(dados_formatados)), 200


@app.route('/hospitais', methods=['GET'])
def get_apelidos():
    entrada =  request.args['hospital']
    hospital_selecionado = request.args['hospital-selecionado'] 
    
    hospitais_encontrados = getApelidos(entrada)
    hospitais_cadastrados = open('hospitais.json', 'r').read()
    hospitais_cadastrados = json.loads(hospitais_cadastrados)
    hospitais_registrados = []
    try:
        hospitais_registrados = hospitais_cadastrados['hospitais'][hospital_selecionado]
    except:
        pass
    if hospitais_encontrados:
        for hospital in hospitais_registrados:
            if hospital in hospitais_encontrados:
                hospitais_encontrados.remove(hospital)
        hospitais = {"hospitais_encontrados": hospitais_encontrados, "hospitais_registrados": hospitais_registrados}
        return make_response(jsonify(hospitais))
    return make_response(jsonify({"status":"Nenhum hospital encontrado"})), 200


def abre_hospital_json_r():
    with open("hospitais.json", "r", encoding='utf-8') as apelidos_json:
                apelidos_json = json.load(apelidos_json)
    return apelidos_json

def abre_hospital_json_drop():
    with open("hospitais_dropdown.json", "r", encoding='utf-8') as hospitais:
                hospitais = json.load(hospitais)
    return hospitais

def abre_hospital_json_w(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(conteudo, arquivo, indent=4)


@app.route("/apelidos", methods=['GET', 'POST', 'DELETE', 'PATCH'])
def apelidos():
    id_hospital = request.args.get('hospital')
    if request.method == 'GET':
       

        if id_hospital is not None:
            hospitais_json = abre_hospital_json_r()
            print(hospitais_json)
            try:
                apelidos = hospitais_json['hospitais'][id_hospital]
                return make_response(jsonify({id_hospital: apelidos})), 200
            except KeyError:
                return make_response(jsonify({"response": "Hospital não encontrado!"})), 404
        else:
            hospitais_json = abre_hospital_json_r()
            return make_response(jsonify(hospitais_json)), 200
    elif request.method == 'POST':
        body = request.json
        print(body)
        hospitais_json = abre_hospital_json_r()
        hospitais_json['hospitais'][list(body.keys())[0]] = body[list(body.keys())[0]]
        abre_hospital_json_w("hospitais.json", hospitais_json)

        return make_response(jsonify(body)), 201
    elif request.method == 'PATCH':
        body = request.json
        apelidos = body[list(body.keys())[0]]
        hospitais_json = abre_hospital_json_r()
        for apelido in apelidos:
            if apelido not in hospitais_json['hospitais'][id_hospital]:
                hospitais_json['hospitais'][id_hospital].append(apelido)
        abre_hospital_json_w("hospitais.json", hospitais_json)

        return make_response(jsonify(body)), 201
    elif request.method == 'DELETE':
        hospitais_json_r = abre_hospital_json_r()
        if id_hospital in hospitais_json_r['hospitais']:
            apelidos = hospitais_json_r['hospitais'][id_hospital]
            del hospitais_json_r['hospitais'][id_hospital]
            abre_hospital_json_w("hospitais.json", hospitais_json_r)
            return make_response(jsonify({id_hospital: apelidos})), 200
        else:
            return make_response(jsonify({"response": "Hospital não encontrado!"})), 404


@app.route("/cadastros/hospitais", methods=['GET', 'POST', 'DELETE'])
def novo_nome_hospital():
    if request.method == 'GET':
        with open('hospitais_dropdown.json', 'r', encoding='utf-8') as hospitais_json:
            hospitais_json = json.load(hospitais_json)
        return make_response(jsonify(hospitais_json))
    
    body = request.json
   
    
    if request.method == 'POST':
        novo_hospital = body['hospital']
        hospitais_json = abre_hospital_json_drop()
        if novo_hospital not in hospitais_json['hospitais']: 
            hospitais_json['hospitais'].append(novo_hospital) 
            abre_hospital_json_w("hospitais_dropdown.json", hospitais_json)
            return make_response(jsonify(
                {"response": "Hospital cadastrado com sucesso!"}
            ), 201)
        else:
            return make_response(
                jsonify({"response": "Hospital já registrado!"}), 200
            )
    
    if request.method == 'DELETE':
        hospitais_a_remover = body['hospitais']
        hospitais_json = abre_hospital_json_drop()
        for novo_hospital in hospitais_a_remover:
            if novo_hospital in hospitais_json['hospitais']:
                hospitais_json['hospitais'].remove(novo_hospital)
        abre_hospital_json_w("hospitais_dropdown.json", hospitais_json)
        return make_response(
            jsonify({"response": f"Hospitais removidos com sucesso!"}), 200
        )

    

if __name__ == '__main__':
    app.run(port = 5000, debug = True)





            
            

    

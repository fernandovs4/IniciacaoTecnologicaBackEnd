from flask import Flask
from flask import request,Response, jsonify, make_response
import json
import re
from flask_cors import CORS
from unidecode import unidecode
from buscaApelidos import getApelidos
from clinicalTrials.getapi import todos_hospitais
app = Flask(__name__)
CORS(app)


    

@app.route('/estudos', methods=['GET'])
def estudos():

    hospitais = todos_hospitais()
    dados = {}
  
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
                            dados[fharma][hospital] = 0
                        else:
                            dados[fharma][hospital] += 1
                else:
                    dados[fharma] = {}
                    if foi:
                        dados[fharma][hospital] = 0
    #     for hospital in LocationFacility:
    #         if hospital not in dados:
    #             dados[hospital] = {}
    #         else:
    #             try:
    #                 if LeadSponsorName[0] not in dados[hospital]:
    #                     dados[hospital][LeadSponsorName[0]] = 0
    #                 else:
    #                     dados[hospital][LeadSponsorName[0]] += 1
    #             except:
    #                 continue
            

    
    
    return make_response(jsonify(dados)), 200


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





            
            

    

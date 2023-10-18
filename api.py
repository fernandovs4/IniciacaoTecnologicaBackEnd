from typing import Any
from flask import Flask, request, make_response, jsonify, Response
from flask_restful import Resource, Api
import json
from unidecode import unidecode
from jsons.buscaApelidos     import getApelidos
from clinicalTrials.getapi import todos_hospitais
from datetime import datetime
from flask_cors import CORS
from filtros.filtradados import filtraDados
from funcoes_auxiliares.valida_data import validaDatas
from funcoes_auxiliares.open_file import abre_hospital_json_r, abre_hospital_json_w, abre_hospital_json_drop
from funcoes_auxiliares.convert_month_year_to_dd__mm_yyyy import convert_month_year_to_dd_mm_yyyy
from pathlib import Path
app = Flask(__name__)
api = Api(app)

CORS(app)
PATH =  Path(__file__).parent.absolute()

def constroi_tabela(data = False, fase=False, idade_min=False, idade_max=False,  status=False,gender=False, stdAge=False):
    dadosTabela = {'estudos':[]}
    dados = todos_hospitais(cache=True)

    dadosTabela = filtraDados(dadosTabela, dados['StudyFieldsResponse']['StudyFields'], data, fase, idade_min, idade_max,status, gender, stdAge)
    return dadosTabela


class ConstruirTabelaResource(Resource):
    def get(self):
        datainicial = False
        datafinal = False
        fase = False
        gender = False
        idade_min = False
        idade_max = False
        status = False
        stdAge = False

        if request.args.get('datainicial') is not None:
            datainicial = request.args['datainicial']
        
        if request.args.get('datafinal') is not None:
            datafinal = request.args['datafinal']
        
        if request.args.get('fase') is not None:
            fase = request.args['fase']
        
        if request.args.get('idade_min') is not None:
            idade_min = request.args['idade_min']
        
        if request.args.get('idade_max') is not None:
            idade_max = request.args['idade_max']
        
        if request.args.get('status') is not None:
            status = request.args['status']
        
        if request.args.get('stdage') is not None:
            stdAge = request.args['stdage']
        
        if request.args.get('gender') is not None:
            gender = request.args['gender']
        
        if datainicial:
            data = [datainicial, datafinal]
        else:
            data = False
        
        tabela = constroi_tabela(data=data, fase=fase, idade_min=idade_min, idade_max=idade_max, status=status, stdAge=stdAge, gender=gender)
        return Response(json.dumps(tabela, ensure_ascii=False).encode('utf8'), mimetype='application/json')




class EstudosResource(Resource):
    def get(self):
        datainicial = ''
        datafinal = ''
        if request.args.get('datainicial') is not None:
            datainicial = request.args['datainicial']
        if request.args.get('datafinal') is not None:
            datafinal = request.args['datafinal']
        
        if request.args.get('cache') is not None:
            if request.args['cache'] == 'true':
                tabelaCache = open(PATH + Path('jsons/cacheTabela.jso'), 'r').read()

                tabelaCache = json.loads(tabelaCache)
                
                return Response(json.dumps(tabelaCache, ensure_ascii=False).encode('utf8'), mimetype='application/json', status=200)

        
        dados = {}
        hospitais = todos_hospitais()
        if datainicial and datafinal:
            if validaDatas(datainicial) != True:
                return validaDatas(datainicial)
            if validaDatas(datafinal) != True:
                return validaDatas(datafinal)
            
            datainicial = datetime.strptime(datainicial, '%d-%m-%Y').date()
            datafinal = datetime.strptime(datafinal, '%d-%m-%Y').date()
            for estudo in hospitais:    
                try:
                    dataEstudo = convert_month_year_to_dd_mm_yyyy(estudo['StartDate'][0])
                    dataEstudo = datetime.strptime(dataEstudo, '%d-%m-%Y').date()
                    if dataEstudo  >= datainicial and dataEstudo <= datafinal:
                        LocationFacility = estudo['LocationFacility']
                        LeadSponsorName = estudo['LeadSponsorName']
                        hospitais_na_base = open(PATH + Path('jsons/hospitais.json' ),'r').read()
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
                hospitais_na_base = open(PATH + Path('jsons/hospitais.json' ),'r').read()
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
        dados_formatados = {}
        for fharma in dados:
            if dados[fharma] != {}:
                dados_formatados[fharma] = dados[fharma]
      
        if dados_formatados == {}:
            return Response(json.dumps({"status":"Nenhum estudo encontrado"}, ensure_ascii=False).encode('utf8'), mimetype='application/json')
        if  not datafinal and not  datainicial:
            with open(PATH + Path('jsons/cacheTabela.json'), 'w') as arquivo:
                json.dump(dados_formatados, arquivo, indent=4)
        return Response(json.dumps(dados_formatados, ensure_ascii=False).encode('utf8'), mimetype='application/json')

class TodosEstudosResource(Resource):
    def get(self):
        hospitais = todos_hospitais(cache= True)
        return Response(json.dumps(hospitais, ensure_ascii=False).encode('utf8'), mimetype='application/json')

class FarmasResource(Resource):
    def get(self):
        hospitais = todos_hospitais(cache= True, farmas = True)
        return Response(json.dumps(hospitais, ensure_ascii=False).encode('utf8'), mimetype='application/json')
class HospitaisResource(Resource):
    def get(self):
        entrada = request.args['hospital']
        hospital_selecionado = request.args['hospital-selecionado'] 
        
        hospitais_encontrados = getApelidos(entrada)
        hospitais_cadastrados = open(PATH + Path('jsons/hospitais.json' ),'r').read()
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
            return Response(json.dumps(hospitais, ensure_ascii=False).encode('utf8'), mimetype='application/json')
        return Response(json.dumps({"status":"Nenhum hospital encontrado"}, ensure_ascii=False).encode('utf8'), mimetype='application/json')

class ApelidosResource(Resource):
    def get(self):
        id_hospital = request.args.get('hospital')

        if id_hospital is not None:
            hospitais_json = abre_hospital_json_r()
            
            try:
                apelidos = hospitais_json['hospitais'][id_hospital]
                return Response(json.dumps(apelidos, ensure_ascii=False).encode('utf8'), mimetype='application/json')
            except KeyError:
                return Response(json.dumps({"status":"Hospital não encontrado"}, ensure_ascii=False).encode('utf8'), mimetype='application/json', status=400)
        else:
            hospitais_json = abre_hospital_json_r()
            return Response(json.dumps(hospitais_json, ensure_ascii=False).encode('utf8'), mimetype='application/json', status=200)

    def post(self):
        body = request.json
      
        hospitais_json = abre_hospital_json_r()
        hospitais_json['hospitais'][list(body.keys())[0]] = body[list(body.keys())[0]]
        abre_hospital_json_w(PATH + Path("jsons/hospitais.json" ),hospitais_json)

        return Response(json.dumps(body), mimetype='application/json', status=201)

    def patch(self):
        id_hospital = request.args.get('hospital')
        body = request.json
        apelidos = body[list(body.keys())[0]]
        hospitais_json = abre_hospital_json_r()
        for apelido in apelidos:
            if apelido not in hospitais_json['hospitais'][id_hospital]:
                hospitais_json['hospitais'][id_hospital].append(apelido)
        abre_hospital_json_w(PATH + Path("jsons/hospitais.json" ),hospitais_json)

        return Response(json.dumps(body), mimetype='application/json', status=200)

    def delete(self):
        id_hospital = request.args.get('hospital')
        hospitais_json_r = abre_hospital_json_r()
        if id_hospital in hospitais_json_r['hospitais']:
            apelidos = hospitais_json_r['hospitais'][id_hospital]
            del hospitais_json_r['hospitais'][id_hospital]
            abre_hospital_json_w(PATH + Path("jsons/hospitais.json" ),hospitais_json_r)
            return Response(json.dumps({"response": "Hospital removido com sucesso!"}), mimetype='application/json', status=200)
        else:
            return Response(json.dumps({"response": "Hospital não encontrado!"}), mimetype='application/json', status=400)

class NovoNomeHospitalResource(Resource):
    def get(self):
        with open(PATH + Path('jsons/hospitais_dropdown'), 'r', encoding='utf-8') as hospitais_json:
            hospitais_json = json.load(hospitais_json)
        return Response(json.dumps(hospitais_json, ensure_ascii=False).encode('utf8'), mimetype='application/json', status=200)

    def post(self):
        body = request.json
        novo_hospital = body['hospital']
        hospitais_json = abre_hospital_json_drop()
        if novo_hospital not in hospitais_json['hospitais']: 
            hospitais_json['hospitais'].append(novo_hospital) 
            abre_hospital_json_w(PATH + Path("jsons/hospitais_dropdwon"), hospitais_json)
            return Response(json.dumps({"response": "Hospital adicionado com sucesso!"}), mimetype='application/json', status=201)
        else:
            return Response(json.dumps({"response": "Hospital já cadastrado!"}), mimetype='application/json', status=400)

    def delete(self):
        body = request.json
        hospitais_a_remover = body['hospitais']
        hospitais_json = abre_hospital_json_drop()
        for novo_hospital in hospitais_a_remover:
            if novo_hospital in hospitais_json['hospitais']:
                hospitais_json['hospitais'].remove(novo_hospital)
        abre_hospital_json_w(PATH + Path("jsons/hospitais_dropdown"), hospitais_json)
        return Response(json.dumps({"response": "Hospital removido com sucesso!"}), mimetype='application/json', status=200)

api.add_resource(EstudosResource, '/estudos')
api.add_resource(HospitaisResource, '/hospitais')
api.add_resource(ApelidosResource, '/apelidos')
api.add_resource(NovoNomeHospitalResource, '/cadastros/hospitais')
api.add_resource(TodosEstudosResource, '/todosEstudos')
api.add_resource(FarmasResource, '/farmas')
api.add_resource(ConstruirTabelaResource, '/construirTabela')
if __name__ == '__main__':
    app.run(port=5000, debug=True)

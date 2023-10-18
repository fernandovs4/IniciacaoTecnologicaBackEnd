import json


def abre_hospital_json_r():
    with open("/home/fernando/WORKSPACE/IniciacaoTecnologica/SistemaWeb/api/apiRegex/hospitais.json", "r", encoding='utf-8') as apelidos_json:
                apelidos_json = json.load(apelidos_json)
    return apelidos_json

def abre_hospital_json_drop():
    with open("hospitais_dropdown.json", "r", encoding='utf-8') as hospitais:
                hospitais = json.load(hospitais)
    return hospitais

def abre_hospital_json_w(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(conteudo, arquivo, indent=4)
        
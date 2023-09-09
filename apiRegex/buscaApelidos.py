from unidecode import unidecode
from pathlib import Path
import re
import json
def getApelidos(hospitalName):
    with open("/home/fernando/WORKSPACE/IniciacaoTecnologica/SistemaWeb/api/apiRegex/clinicalTrials/todosHospitais.json", 'r',  encoding='utf-8') as hospitais:
        hospitais = json.load(hospitais)
        hospitais_encontrados = {"hospitais": []}
        hospital_unidecode= unidecode(hospitalName)
        for hospital in hospitais["hospitais"]:
            try:
                if re.findall(hospital_unidecode, unidecode(hospital), re.IGNORECASE) and  (hospital not in hospitais_encontrados["hospitais"]):
                        hospitais_encontrados['hospitais'].append(hospital)
            except:
                continue
    return hospitais_encontrados
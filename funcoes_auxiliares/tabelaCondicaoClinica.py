from pathlib import Path
PATH = Path(__file__).parent.parent
import json
dados = {}
hospital_na_base = open(PATH / Path('jsons/hospitais.json' ),'r').read()
hospital_na_base = json.loads(hospital_na_base)['hospitais']

def tabela_condicao_clinica(estudos):
    res = {}
    for estudo in estudos['estudos']:
        condicao = estudo['Condition'][0]
        LocationFacility = estudo['LocationFacility']
        if len(LocationFacility) > 0:
            for hospital in LocationFacility:
                for apelido in hospital_na_base.items():
                    if hospital in apelido[1]:
                        if apelido[0] not in res:
                            res[apelido[0]] = {condicao: 1}
                        else:
                            if condicao not in res[apelido[0]]:
                                res[apelido[0]][condicao] = 1
                            else:
                                res[apelido[0]][condicao] += 1
                        break
    
    return res
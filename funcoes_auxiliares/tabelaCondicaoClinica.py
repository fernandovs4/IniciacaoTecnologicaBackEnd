from pathlib import Path
PATH = Path(__file__).parent.parent
import json
import copy
dados = {}
hospital_na_base = open(PATH / Path('jsons/hospitais.json' ),'r').read()
hospital_na_base = json.loads(hospital_na_base)['hospitais']

def tabela_condicao_clinica(estudos, inversed, simetric):
    res = {}
    for estudo in estudos['estudos']:
        condicao = estudo['Condition'][0]
        LocationFacility = estudo['LocationFacility']
        if len(LocationFacility) > 0:
            if not inversed:
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
            else:
                molde = {f"{hosp}": 0 for hosp in hospital_na_base.keys()}
                for hospital in LocationFacility:
                    for apelido in hospital_na_base.items():
                        if hospital in apelido[1]:
                            if condicao in res:
                                if apelido[0] in res[condicao]:
                                    res[condicao][apelido[0]] += 1
                                else:
                                    res[condicao][apelido[0]] = 1
                            else:
                                res[condicao] = copy.deepcopy(molde)
                                res[condicao][apelido[0]] = 1
    if not simetric:
            res_simetric = {}
            for item in res.items():
                novo_el = {}
                for el in item[1].items():
                    if el[1] != 0:
                        novo_el[el[0]] = el[1]
                res_simetric[item[0]] = novo_el
            res = res_simetric    
    return res
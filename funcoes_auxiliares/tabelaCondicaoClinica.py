from pathlib import Path
PATH = Path(__file__).parent.parent
import json
import copy
import time
dados = {}
hospital_na_base = open(PATH / Path('jsons/hospitais.json' ),'r').read()
hospital_na_base = json.loads(hospital_na_base)['hospitais']
print(hospital_na_base.keys())
def soma_quantidades(doeca_data):
        return sum(doeca_data.values())

def ordenar_valores(doeca_data):
        return dict(sorted(doeca_data.items(), key=lambda item: item[1], reverse=True))

    # Função para calcular a soma das quantidades para uma doença
def soma_quantidades(doeca_data):
    return sum(doeca_data.values())

def tabela_clinica_condicao(estudos, inversed, simetric, sort_interno, sort_externo, total_externo, total_interno):
    res = {}
    estudos_condicoes =[]
    for estudo in estudos['estudos']:
        try:
            condicao = estudo['Condition'][0]
        except:
            continue
        if condicao not in estudos_condicoes:
            estudos_condicoes.append(condicao)
   
    molde = {}
    for hosp in  hospital_na_base.keys():
        molde[hosp] = {}
        for condicao in estudos_condicoes:
            molde[hosp][condicao] = 0


    molde2 = {f"{hosp}": 0 for hosp in hospital_na_base.keys()}
    for estudo in estudos['estudos']:
        try:
            try:
                condicao = estudo['Condition'][0]
            except:
                continue
            LocationFacility = estudo['LocationFacility']
            if len(LocationFacility) > 0:
                if inversed:
                    for hospital in LocationFacility:
                        for apelido in hospital_na_base.items():
                            if hospital in apelido[1]:
                                try:
                                    if apelido[0] in res:
                                            res[apelido[0]][condicao] += 1
                                    else:
                                        res = copy.deepcopy(molde)
                                        res[apelido[0]][condicao] = 1
                                except KeyError as e :
                                    continue
                                
                else:
                
                    for hospital in LocationFacility:
                        for apelido in hospital_na_base.items():
                            if hospital in apelido[1]:
                                if condicao in res:
                                        res[condicao][apelido[0]] += 1
                                else:
                                    res[condicao] = copy.deepcopy(molde2)
                                    res[condicao][apelido[0]] = 1
        except KeyError as e :
            continue
    if not simetric:
            res_simetric = {}
            for item in res.items():
                novo_el = {}
                for el in item[1].items():
                    if el[1] != 0:
                        novo_el[el[0]] = el[1]
                res_simetric[item[0]] = novo_el
            res = res_simetric    
    
    if total_interno:
            res['Total'] = {}
            for farma in res:
                if farma != 'Total':
                    for hospital in res[farma]:
                        if hospital in res['Total']:
                            res['Total'][hospital] += res[farma][hospital]
                        else:
                            res['Total'][hospital] = res[farma][hospital]
            res['Total'] = ordenar_valores(res['Total'])
        
    novo_res = {}
    if total_externo:
            
            for farma in res.keys():
                soma = sum(list(res[farma].values()))
                novo_res[farma] = res[farma]
                novo_res[farma]['Total'] = soma
            res = novo_res
        
    if sort_externo:
        # Ordena as doenças com base na soma das quantidades dos hospitais (em ordem decrescente)
        res = dict(sorted(res.items(), key=lambda item: sum(item[1].values()), reverse=True))
    
    
    if sort_interno:
        # Ordena as doenças com base na soma das quantidades dos hospitais (em ordem decrescente)
        res = {doenca: ordenar_valores(valores) for doenca, valores in sorted(res.items(), key=lambda item: soma_quantidades(item[1]), reverse=True)}

    return res
from pathlib import Path
PATH = Path(__file__).parent.parent
import json
import copy
dados = {}

def soma_quantidades(doeca_data):
        return sum(doeca_data.values())

def soma_quantidades(doeca_data):
        return sum(doeca_data.values())

def ordenar_valores(doeca_data):
        return dict(sorted(doeca_data.items(), key=lambda item: item[1], reverse=True))

def tabela_condicao_farma(estudos, inversed, simetric, sort_interno, sort_externo, total_externo, total_interno):
    res = {}
    molde = {}
    if not inversed:
       
        for estudo in estudos['estudos']:
            if estudo['LeadSponsorName'][0] not in molde:
                molde[estudo['LeadSponsorName'][0]] = 0
        for estudo in estudos['estudos']:
            condicao = estudo['Condition'][0]
            LeadSponsorName = estudo['LeadSponsorName']
            if len(LeadSponsorName) > 0:
                if condicao in res:
                        res[condicao][LeadSponsorName[0]] += 1
                else:
                    res[condicao] = copy.deepcopy(molde)
                    res[condicao][LeadSponsorName[0]] = 1
    else:
        for estudo in estudos['estudos']:
            if estudo['Condition'][0] not in molde:
                molde[estudo['Condition'][0]] = 0

        for estudo in estudos['estudos']:
            condicao = estudo['Condition'][0]
            LeadSponsorName = estudo['LeadSponsorName']
            if len(LeadSponsorName) > 0:
                if LeadSponsorName[0] in res:
                    if condicao in res[LeadSponsorName[0]]:
                        res[LeadSponsorName[0]][condicao] += 1
                    else:
                        res[LeadSponsorName[0]][condicao] = 1
                else:
                    res[LeadSponsorName[0]] = copy.deepcopy(molde)
                    res[LeadSponsorName[0]][condicao] = 1
    if not simetric:
            res_simetric = {}
            for item in res.items():
                novo_el = {}
                for el in item[1].items():
                    if el[1] != 0:
                        novo_el[el[0]] = el[1]
                res_simetric[item[0]] = novo_el
            res = res_simetric
    if total_externo:
            res['total_externo'] = {}
            for farma in res:
                if farma != 'total_externo':
                    for hospital in res[farma]:
                        if hospital in res['total_externo']:
                            res['total_externo'][hospital] += res[farma][hospital]
                        else:
                            res['total_externo'][hospital] = res[farma][hospital]
            res['total_externo'] = ordenar_valores(res['total_externo'])
        
    if sort_externo:
    # Ordena as doenças com base na soma das quantidades dos hospitais (em ordem decrescente)
        res = dict(sorted(res.items(), key=lambda item: sum(item[1].values()), reverse=True))
    
  
    if sort_interno:
        # Ordena as doenças com base na soma das quantidades dos hospitais (em ordem decrescente)
        res = {doenca: ordenar_valores(valores) for doenca, valores in sorted(res.items(), key=lambda item: soma_quantidades(item[1]), reverse=True)}


    return res
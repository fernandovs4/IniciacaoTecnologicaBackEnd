from pathlib import Path
PATH = Path(__file__).parent.parent
import json
import copy
dados = {}
def tabela_condicao_farma(estudos, inversed, simetric):
    res = {}
    if inversed:
        molde = {}
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
            condicao = estudo['Condition'][0]
            LeadSponsorName = estudo['LeadSponsorName']
            if len(LeadSponsorName) > 0:
                if LeadSponsorName[0] in res:
                    if condicao in res[LeadSponsorName[0]]:
                        res[LeadSponsorName[0]][condicao] += 1
                    else:
                        res[LeadSponsorName[0]][condicao] = 1
                else:
                    res[LeadSponsorName[0]] = {}
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
    return res
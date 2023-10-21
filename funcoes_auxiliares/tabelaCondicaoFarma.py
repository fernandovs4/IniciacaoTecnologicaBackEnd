from pathlib import Path
PATH = Path(__file__).parent.parent
import json
dados = {}
def tabela_condicao_farma(estudos):
    res = {}
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
    return res
from pathlib import Path
PATH = Path(__file__).parent.parent
import json
import copy

dados = {}
def tabela_farma_clinica(estudos, inversed, simetric):
        res = {}
        hospitais_na_base = open(PATH / Path('jsons/hospitais.json' ),'r').read()
        hospitais_na_base = json.loads(hospitais_na_base)['hospitais']
        if inversed:
            molde ={f"{hosp}": 0 for hosp in json.loads(open(PATH / Path('jsons/hospitais.json' ),'r').read())['hospitais'].keys()}
            for estudo in estudos['estudos']:
                LocationFacility = estudo['LocationFacility']
                LeadSponsorName = estudo['LeadSponsorName'][0]
                
                if len(LocationFacility) > 0:
                    for hospital in LocationFacility:
                        for apelido in hospitais_na_base.items():
                            if hospital in apelido[1]:
                                if LeadSponsorName in res:
                                    res[LeadSponsorName][apelido[0]] += 1
                                else:
                                    res[LeadSponsorName] = copy.deepcopy(molde)
                                    res[LeadSponsorName][apelido[0]] = 1 
                                                  
        else:
            molde = {f"{farma['LeadSponsorName'][0]}": 0 for farma in estudos['estudos']}
            for estudo in estudos['estudos']:
                LocationFacility = estudo['LocationFacility']
                LeadSponsorName = estudo['LeadSponsorName'][0]

                if len(LocationFacility) > 0:
                    for hospital in LocationFacility:
                        for apelido in hospitais_na_base.items():
                            if hospital in apelido[1]:
                                if apelido[0] in res:
                                        res[apelido[0]][LeadSponsorName] += 1
                                else:
                                    res[apelido[0]] = copy.deepcopy(molde)
                                    res[apelido[0]][LeadSponsorName] = 1
                                break
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
       
                            
                        

























        #             fharma = LeadSponsorName[0]
        #             for hospital in LocationFacility:
        #                 foi = False
        #                 for apelido in hospitais_na_base.items():
        #                     if hospital in apelido[1]:
        #                         hospital = apelido[0]
        #                         foi = True
        #                         break
        #                 if fharma in dados:
                        
        #                     if foi:
        #                         if hospital not in dados[fharma]:
        #                             dados[fharma][hospital] = 1
        #                         else:
        #                             dados[fharma][hospital] += 1
        #                 else:
        #                     dados[fharma] = {}
        #                     if foi:
        #                         dados[fharma][hospital] = 1
        # dados_formatados = {}
        # for fharma in dados:
        #     if dados[fharma] != {}:
        #         dados_formatados[fharma] = dados[fharma]
        # return dados_formatados
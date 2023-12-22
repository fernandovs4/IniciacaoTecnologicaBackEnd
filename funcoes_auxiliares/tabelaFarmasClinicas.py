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

def tabela_farma_clinica(estudos, inversed, simetric, sort_interno, sort_externo, total_externo, total_interno):
        res = {}
        
        hospitais_na_base = open(PATH / Path('jsons/hospitais.json' ),'r').read()
        hospitais_na_base = json.loads(hospitais_na_base)['hospitais']
        if inversed:
            molde ={f"{hosp}": 0 for hosp in json.loads(open(PATH / Path('jsons/hospitais.json' ),'r').read())['hospitais'].keys()}
            for estudo in estudos['estudos']:
                LocationFacility = estudo['LocationFacility']
                try:
                    LeadSponsorName = estudo['LeadSponsorName'][0]
                except KeyError as e :
                    continue
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
                try:
                    LeadSponsorName = estudo['LeadSponsorName'][0]
                except KeyError as e :
                    continue

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
import copy

def soma_quantidades(doeca_data):
        return sum(doeca_data.values())

def soma_quantidades(doeca_data):
        return sum(doeca_data.values())

def ordenar_valores(doeca_data):
        return dict(sorted(doeca_data.items(), key=lambda item: item[1], reverse=True))

def tabela_fase_condicao(estudos, inversed=False, simetric=False, sort_interno=False, sort_externo=False, total_externo=False, total_interno=False):
    res = {"Total": {"Total":0}, "fase 1": {"Total":0}, "fase 2": {"Total":0}, "fase 3": {"Total":0}, "fase 4": {"Total":0}, "sem fase": {"Total":0}, "Nao aplicavel": {"Total":0}, "fase inicial": {"Total":0} }
    if inversed:
        res = {"Total":{"Total": 0, "fase 1": 0, "fase 2": 0, "fase 3": 0, "fase 4": 0, "sem fase": 0, "Nao aplicavel": 0, "fase inicial": 0}}

    for estudo in estudos['estudos']:
            if inversed:
                conditions = estudo['Condition']
                for condition in conditions:
                    fase = estudo['Phase']
                    if condition not in  res:
                        res[condition] = {"Total": 0 ,"fase 1": 0, "fase 2": 0, "fase 3": 0, "fase 4": 0, "sem fase": 0, "Nao aplicavel": 0}
                        if fase == []:
                            res[condition]["sem fase"] += 1
                            res[condition]["Total"] += 1
                            res["Total"]["sem fase"] += 1

                        elif fase == ['Not Applicable']:
                            res[condition]["Nao aplicavel"] += 1
                            res[condition]["Total"] += 1
                            res["Total"]["Nao aplicavel"] += 1
                        else:
                            for f in fase:
                                res[condition]["fase " + f.split(" ")[1]] += 1
                                res[condition]["Total"] += 1
                                res["Total"]["fase " + f.split(" ")[1]] += 1
                        
                    else:
                        if fase == []:
                            res[condition]["sem fase"] += 1
                            res[condition]["Total"] += 1
                            res["Total"]["sem fase"] += 1
                        elif fase == ['Not Applicable']:
                            res[condition]["Nao aplicavel"] += 1
                            res[condition]["Total"] += 1
                            res["Total"]["Nao aplicavel"] += 1
                        else:
                            res[condition]["fase " + fase[0].split(" ")[1]] += 1
                            res[condition]["Total"] += 1
                            res["Total"]["fase " + fase[0].split(" ")[1]] += 1

            else:
                conditions = estudo['Condition']
                for condition in conditions:
                    fase = estudo['Phase']
                    if fase == []:
                        if condition in res["sem fase"]:
                            res["sem fase"][condition] += 1
                            res["sem fase"]["Total"] += 1
                            if condition in res["Total"]:
                                res["Total"][condition] += 1
                            else:
                                res["Total"][condition] = 1
                        else:
                            res["sem fase"][condition] = 1
                            res["sem fase"]["Total"] += 1
                            if condition in res["Total"]:
                                res["Total"][condition] += 1
                            else:
                                res["Total"][condition] = 1
                    elif fase == ['Not Applicable']:
                        if condition in res["Nao aplicavel"]:
                            res["Nao aplicavel"][condition] += 1
                            res["Nao aplicavel"]["Total"] += 1
                            if condition in res["Total"]:
                                res["Total"][condition] += 1
                            else:
                                res["Total"][condition] = 1
                        else:
                            res["Nao aplicavel"][condition] = 1
                            res["Nao aplicavel"]["Total"] += 1
                            if condition in res["Total"]:
                                res["Total"][condition] += 1
                            else:
                                res["Total"][condition] = 1
                   
                    else:
                        for f in fase:
                            
                                if f == 'Early Phase 1':
                                    f = 'fase inicial'
                                if condition in res["fase " + f.split(' ')[1]]:
                                    res["fase " + f.split(" ")[1]][condition] += 1
                                    res["fase " + f.split(" ")[1]]["Total"] += 1
                                    if condition in res["Total"]:
                                        res["Total"][condition] += 1
                                    else:
                                        res["Total"][condition] = 1
                                else:
                                    res["fase " + f.split(" ")[1]][condition] = 1
                                    res["fase " + f.split(" ")[1]]["Total"] += 1
                                    if condition in res["Total"]:
                                        res["Total"][condition] += 1
                                    else:
                                        res["Total"][condition] = 1
                           
                                 
    res["Total"]["Total"] = sum(res["Total"].values())

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
    
import copy

def tabela_fase_farma(estudos, inversed = False, simetric=False, sort_interno=False, sort_externo=False, total_externo=False, total_interno=False):
    
    fases = {"Total": {"Total": 0}, "fase 1": {"Total":0}, "fase 2": {"Total":0}, "fase 3": {"Total":0}, "fase 4": {"Total":0}, "sem fase": {"Total":0}, "Nao aplicavel": {"Total":0}}
    if inversed:
        fases = {"Total": {"Total": 0, "fase 1":0, "fase 2": 0, "fase 3": 0, "fase 4": 0, "sem fase": 0, "Nao aplicavel": 0}}

    for estudo in estudos['estudos']:
            if inversed:
                LeadSponsorName = estudo['LeadSponsorName'][0]
                fase = estudo['Phase']
                if LeadSponsorName not in  fases:
                    fases[LeadSponsorName] = {"Total": 0, "fase 1": 0, "fase 2": 0, "fase 3": 0, "fase 4": 0, "sem fase": 0, "Nao aplicavel": 0}
                    if fase == []:
                        fases[LeadSponsorName]["sem fase"] += 1
                        fases[LeadSponsorName]["Total"] += 1
                        fases["Total"]["sem fase"] += 1

                    elif fase == ['Not Applicable']:
                        fases[LeadSponsorName]["Nao aplicavel"] += 1
                        fases[LeadSponsorName]["Total"] += 1
                        fases["Total"]["Nao aplicavel"] += 1

                    else:
                        for f in fase:
                            fases[LeadSponsorName]["fase " + f.split(" ")[1]] += 1
                            fases[LeadSponsorName]["Total"] += 1
                            fases["Total"]["fase " + f.split(" ")[1]] += 1

                
                    
                else:
                    if fase == []:
                        fases[LeadSponsorName]["sem fase"] += 1
                        fases[LeadSponsorName]["Total"] += 1
                        fases["Total"]["sem fase"] += 1

                    elif fase == ['Not Applicable']:
                        fases[LeadSponsorName]["Nao aplicavel"] += 1
                        fases[LeadSponsorName]["Total"] += 1
                        fases["Total"]["Nao aplicavel"] += 1
                    else:
                        for f in fase:
                            fases[LeadSponsorName]["fase " + f.split(" ")[1]] += 1
                            fases[LeadSponsorName]["Total"] += 1  
                            fases["Total"]["fase " + f.split(" ")[1]] += 1

            

            else:
                LeadSponsorName = estudo['LeadSponsorName'][0]
                fase = estudo['Phase']
                if fase == []:
                    if LeadSponsorName in fases["sem fase"]:
                        fases["sem fase"][LeadSponsorName] += 1
                        fases["sem fase"]["Total"] += 1
                        if LeadSponsorName in fases["Total"]:
                            fases["Total"][LeadSponsorName] += 1
                        else:
                            fases["Total"][LeadSponsorName] = 1
                     

                    else:
                        fases["sem fase"][LeadSponsorName] = 1
                        fases["sem fase"]["Total"] += 1
                        if LeadSponsorName in fases["Total"]:
                            fases["Total"][LeadSponsorName] += 1
                        else:
                            fases["Total"][LeadSponsorName] = 1
                elif fase == ['Not Applicable']:
                    if LeadSponsorName in fases["Nao aplicavel"]:
                        fases["Nao aplicavel"][LeadSponsorName] += 1
                        fases["Nao aplicavel"]["Total"] += 1
                        if LeadSponsorName in fases["Total"]:
                            fases["Total"][LeadSponsorName] += 1
                        else:
                            fases["Total"][LeadSponsorName] = 1
                    else:
                        fases["Nao aplicavel"][LeadSponsorName] = 1
                        fases["Nao aplicavel"]["Total"] += 1
                        if LeadSponsorName in fases["Total"]:
                            fases["Total"][LeadSponsorName] += 1
                        else:
                            fases["Total"][LeadSponsorName] = 1
                else:
                    for f in fase:
                        if LeadSponsorName in fases["fase " + f.split(' ')[1]]:
                            fases["fase " + f.split(" ")[1]][LeadSponsorName] += 1
                            fases["fase " + f.split(" ")[1]]["Total"] += 1
                            if LeadSponsorName in fases["Total"]:
                                fases["Total"][LeadSponsorName] += 1

                            else:
                                fases["Total"][LeadSponsorName] = 1

                        else:
                            fases["fase " + f.split(" ")[1]][LeadSponsorName] = 1
                            fases["fase " + f.split(" ")[1]]["Total"] += 1
                            if LeadSponsorName in fases["Total"]:
                                fases["Total"][LeadSponsorName] += 1

                            else:
                                fases["Total"][LeadSponsorName] = 1


    fases['Total']['Total'] =  sum(fases["Total"].values())
    
    return fases
    return res
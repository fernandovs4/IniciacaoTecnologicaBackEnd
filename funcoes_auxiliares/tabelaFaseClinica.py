import copy
import json
from pathlib import Path
PATH = Path(__file__).parent.parent
def tabela_fase_clinica(estudos, inversed = False, simetric = False, sort_interno = False, sort_externo=False, total_externo=False, total_interno=False):
    clinicas_ = open(PATH / Path('jsons/hospitais.json' ),'r').read()
    clinicas = list(dict(json.loads(clinicas_)['hospitais']).keys())
    fases_por_clinica = {}
    fases_por_clinica["Total"] = {"Total": 0 , "fase 1":0, "fase 2":0, "fase 3":0, "fase 4":0, "sem fase": 0, "Nao aplicavel": 0}
    for centro in clinicas:
        fases_por_clinica[centro] = {"Total": 0 , "fase 1":0, "fase 2":0, "fase 3":0, "fase 4":0, "sem fase": 0, "Nao aplicavel": 0}
    if inversed:
        fases_por_clinica = {"Total": {"Total": 0 }, "fase 1":{"Total": 0}, "fase 2":{"Total":0}, "fase 3":{"Total":0}, "fase 4":{"Total":0}, "sem fase": {"Total":0}, "Nao aplicavel": {"Total": 0}}
   
    for estudo in estudos['estudos']:
        apelidos_ = dict(json.loads(clinicas_)['hospitais']).items()
        if inversed:
            if estudo['Phase']== []:
                for centro in estudo['LocationFacility']:
                    for c, apelidos in apelidos_:
                        if centro in apelidos:
                            if c in fases_por_clinica["sem fase"]:
                                fases_por_clinica["sem fase"][c] += 1
                                fases_por_clinica["sem fase"]["Total"] += 1
                                if c in fases_por_clinica["Total"]:
                                    fases_por_clinica["Total"][c] += 1
                                else:
                                    fases_por_clinica["Total"][c] = 1
                            else:
                                fases_por_clinica["sem fase"][c] = 1
                                fases_por_clinica["sem fase"]["Total"] += 1
                                if c in fases_por_clinica["Total"]:
                                    fases_por_clinica["Total"][c] += 1
                                else:
                                    fases_por_clinica["Total"][c] = 1
                           
            elif estudo['Phase'] == ['Not Applicable']:
                for centro in estudo['LocationFacility']:
                    for c, apelidos in apelidos_:
                        if centro in apelidos:
                            if c in fases_por_clinica["Nao aplicavel"]:
                                fases_por_clinica["Nao aplicavel"][c] += 1
                                fases_por_clinica["Nao aplicavel"]["Total"] += 1
                                if c in fases_por_clinica["Total"]:
                                    fases_por_clinica["Total"][c] += 1
                                else:
                                    fases_por_clinica["Total"][c] = 1
                            else:
                                fases_por_clinica["Nao aplicavel"][c] = 1
                                fases_por_clinica["Nao aplicavel"]["Total"] += 1
                                if c in fases_por_clinica["Total"]:
                                    fases_por_clinica["Total"][c] += 1
                                else:
                                    fases_por_clinica["Total"][c] = 1
                           
            else:
                for fase in estudo['Phase']:
                    if len(estudo['Phase']) > 1:
                        print(estudo['Phase'])
                    for centro in estudo['LocationFacility']:
                        for c, apelidos in apelidos_:
                            if centro in apelidos:
                                if c in fases_por_clinica[f"fase {fase.split(' ')[1]}"]:
                                    fases_por_clinica[f"fase {fase.split(' ')[1]}"][c] += 1
                                    fases_por_clinica[f"fase {fase.split(' ')[1]}"]["Total"] += 1
                                    if c in fases_por_clinica["Total"]:
                                        fases_por_clinica["Total"][c] += 1
                                    else:
                                        fases_por_clinica["Total"][c] = 1
                                else:
                                    fases_por_clinica[f"fase {fase.split(' ')[1]}"][c] = 1
                                    fases_por_clinica[f"fase {fase.split(' ')[1]}"]["Total"] += 1
                                    if c in fases_por_clinica["Total"]:
                                        fases_por_clinica["Total"][c] += 1
                                    else:
                                        fases_por_clinica["Total"][c] = 1
                                
        else:
            if estudo['Phase']== []:
                for centro in estudo['LocationFacility']:
                    for c, apelidos in apelidos_:
                        if centro in apelidos:
                            fases_por_clinica[c]["sem fase"] += 1
                            fases_por_clinica[c]["Total"] += 1
                            fases_por_clinica["Total"]["sem fase"] += 1
            elif estudo['Phase'] == ['Not Applicable']:
                for centro in estudo['LocationFacility']:
                    for c, apelidos in apelidos_:
                        if centro in apelidos:
                            fases_por_clinica[c]["Nao aplicavel"] += 1
                            fases_por_clinica[c]["Total"] += 1
                            fases_por_clinica["Total"]["Nao aplicavel"] += 1
            else:
                for fase in estudo['Phase']:
                    for centro in estudo['LocationFacility']:
                        for c, apelidos in apelidos_:
                            if centro in apelidos:
                                fases_por_clinica[c][f"fase {fase.split(' ')[1]}"] += 1
                                fases_por_clinica[c]["Total"] += 1
                                fases_por_clinica["Total"][f"fase {fase.split(' ')[1]}"] += 1
    fases_por_clinica["Total"]["Total"] = sum([fases_por_clinica["Total"][c] for c in fases_por_clinica["Total"]])
    
    return fases_por_clinica




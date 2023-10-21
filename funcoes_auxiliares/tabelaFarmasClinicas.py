from pathlib import Path
PATH = Path(__file__).parent.parent
import json
dados = {}
def tabela_farma_clinica(estudos):
        for estudo in estudos['estudos']:
                LocationFacility = estudo['LocationFacility']
                LeadSponsorName = estudo['LeadSponsorName']
                hospitais_na_base = open(PATH / Path('jsons/hospitais.json' ),'r').read()
                hospitais_na_base = json.loads(hospitais_na_base)['hospitais']
                if len(LeadSponsorName) > 0:
                    fharma = LeadSponsorName[0]
                    for hospital in LocationFacility:
                        foi = False
                        for apelido in hospitais_na_base.items():
                            if hospital in apelido[1]:
                                hospital = apelido[0]
                                foi = True
                                break
                        if fharma in dados:
                        
                            if foi:
                                if hospital not in dados[fharma]:
                                    dados[fharma][hospital] = 1
                                else:
                                    dados[fharma][hospital] += 1
                        else:
                            dados[fharma] = {}
                            if foi:
                                dados[fharma][hospital] = 1
        dados_formatados = {}
        for fharma in dados:
            if dados[fharma] != {}:
                dados_formatados[fharma] = dados[fharma]
        return dados_formatados
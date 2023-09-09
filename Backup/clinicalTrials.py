import requests
# dicDeEstudos = {'total':{ "ICESP": 0,"AC Camargo": 0, "Einstein": 0, "Moinhos": 0, "Beneficencia": 0, "ABC": 0, "COI": 0, "Araújo Jorge": 0, "Barretos": 0, "Mãe de Deus": 0, "Rio Preto": 0, "Sírios Libanês": 0, "Unifesp": 0, "Ijui": 0, "HCPA":0, "Albert eintein":0, "Oswaldo Cruz":0,"Unicamp":0, "Jaú":0, "Rio Preto":0, "Rede D'or":0, 'total':0}}
# dicEstudosPorDatas = {}
# dicCondition = {"total":{}}
# import json
# hosp = ["A.C Camargo", "Sírio Libanês", "Albert Einstein", "Moinhos de Vento", "Beneficencia Portuguesa", "Instituto Nacional do Cancer", "CEPHO ", "Instituto Brasileiro de Controle do Cancer", "PUCRS", "CEPON", "Hospital do Cancer de Barretos", "Faculdade de Medicina do ABC", "Faculdade de Medicina do ABC", "FMUSP", "COI ", "ICESP", "Alexander Fleming", "D'or", "Erasto Gaertner", "Araujo Jorge","Senhora da Conceica", "Mae de Deus", "Oswaldo Cruz", "Caridade de Ijui"]

# with open("hospitais.json") as f:
#     f = json.load(f)["hospitais"]
# hospitais = f
# print(hospitais['ABC'])
import json
min_rank = 1
max_rank = 100
query = {
    'expr' : 'cancer AND  AREA[LeadSponsorClass]Industry AND SEARCH[Location](AREA[LocationCountry]Brasil)',
    'fields' : 'LeadSponsorClass,LeadSponsorName,LocationFacility, LocationCountry,StartDate, Condition,Phase',
    'fmt' : 'JSON',   
    'min_rnk' : min_rank,
    'max_rnk' : max_rank
}

url = "http://ClinicalTrials.gov/api/query/study_fields"

todos_hospitais = []
brasil = []
j = 0 
soma = 0
response = requests.get(url, params=query)
data = response.json()
print(data)
# while True:

 
#         response = requests.get(url, params=query) #, headers=headers)
#         query['min_rnk'] += 100
#         query['max_rnk'] += 100
#         if response.status_code != 200:
#             print(response.status_code)
#             break
#         if query['min_rnk'] == 1501:
#             break

   
#         data = response.json()
#         print(query['min_rnk'])
#         print(len(data))
#         for estudo in data['StudyFieldsResponse']['StudyFields']:
#         #             print(estudo['LocationFacility'])
#                     # for hospital_ in estudo['LocationFacility'] :
#                     #     if hospital_ not in todos_hospitais:
#                     #         todos_hospitais.append(hospital_)
#                     #         print(hospital_)
#                     if len(estudo['StartDate']) ==1:
                                
#                                  a = estudo['StartDate'][0].split(" ")
#                                  data = int(a[-1])
#                                  if(data >= 2020 and data <= 2021):

#                                     if estudo['LeadSponsorName'][0] not in dicDeEstudos:
                                        
#                                         dicDeEstudos[estudo['LeadSponsorName'][0]] = {  "ICESP": 0,"AC Camargo": 0, "Einstein": 0, "Moinhos": 0, "Beneficencia": 0, "ABC": 0, "COI": 0, "Araújo Jorge": 0, "Barretos": 0, "Mãe de Deus": 0, "Rio Preto": 0, "Sírios Libanês": 0, "Unifesp": 0, "Ijui": 0, "HCPA":0, "Albert eintein":0, "Oswaldo Cruz":0,"Unicamp":0, "Jaú":0, "Rio Preto":0, "Rede D'or":0, "total": 0}
                                    
                                    
#                                     for nome_hosp, apelidos  in hospitais.items():
#                                         for apelido in apelidos:
#                                             if apelido in str(estudo['LocationFacility']):
#                                                 print(apelido, nome_hosp)
#                                                 dicDeEstudos[estudo['LeadSponsorName'][0]][nome_hosp] += 1 
#                                                 dicDeEstudos[estudo['LeadSponsorName'][0]]['total'] += 1 
                                            
#                                                 dicDeEstudos['total'][nome_hosp] += 1 
#                                                 dicDeEstudos['total']['total'] += 1 


                        
#                     #     if hospital in str(estudo['LocationFacility']):
#                     #         dicDeEstudos[estudo['LeadSponsorName'][0]][hosp[i]] += 1 
#                     #         print("passou", j)
#                     #         if len(estudo['StartDate']) ==1:
                                
#                     #             a = estudo['StartDate'][0].split(" ")
                                
#                     #             j+=1
#                     #             if a[-1] not in dicEstudosPorDatas:
#                     #                 dicEstudosPorDatas[a[-1]] = { "A.C Camargo": 0, "Sírio Libanês": 0, "Albert Einstein": 0, "Moinhos de Vento": 0, "Beneficencia Portuguesa": 0, "Instituto Nacional do Cancer": 0, "CEPHO ": 0, "Instituto Brasileiro de Controle do Cancer": 0, "PUCRS": 0, "CEPON": 0, "Hospital do Cancer de Barretos": 0, "Faculdade de Medicina do ABC": 0, "FMUSP": 0, "COI ": 0, "ICESP": 0, "Alexander Fleming": 0, "D'or": 0, "Erasto Gaertner": 0, "Araujo Jorge": 0, "Senhora da Conceica": 0, "Mae de Deus": 0, "Oswaldo Cruz": 0, "Caridade de Ijui": 0}
#                     #             else:
#                     #                 dicEstudosPorDatas[a[-1]][hosp[i]] += 1 

#                     #     if len(estudo['Condition'])>= 1:
#                     #             for cond in estudo['Condition']:
#                     #                 if cond not in dicCondition:
#                     #                     dicCondition[cond] = { "A.C Camargo": 0, "Sírio Libanês": 0, "Albert Einstein": 0, "Moinhos de Vento": 0, "Beneficencia Portuguesa": 0, "Instituto Nacional do Cancer": 0, "CEPHO ": 0, "Instituto Brasileiro de Controle do Cancer": 0, "PUCRS": 0, "CEPON": 0, "Hospital do Cancer de Barretos": 0, "Faculdade de Medicina do ABC": 0, "FMUSP": 0, "COI ": 0, "ICESP": 0, "Alexander Fleming": 0, "D'or": 0, "Erasto Gaertner": 0, "Araujo Jorge": 0, "Senhora da Conceica": 0, "Mae de Deus": 0, "Oswaldo Cruz": 0, "Caridade de Ijui": 0}
#                     #                 else:
#                     #                     dicCondition[cond][hosp[i]] += 1

     
# # with open('todos_hospitais.txt', 'w') as f:
# #     f.write(str(todos_hospitais))
# #     f.close()
  
# # with open ('todos_hospitais_por_linha.txt', 'w') as f:
# #     for hosp3 in todos_hospitais:
# #         f.write(hosp3 + " \n")
# #     f.close()
# dicDeEstudos2 = {}
# for chave, valor in dicDeEstudos.items():
#     if valor['total'] != 0  and (chave != "Cristália Produtos Químicos Farmacêuticos Ltda." or chave != "Crist�lia Produtos Qu�micos Farmac�uticos Ltda."):
#         dicDeEstudos2[chave] = valor
# with open('EstudoPorFarma.txt', 'w') as f:
#     f.write(str(dicDeEstudos2))
#     f.close()
# # with open('EstudoPorData.txt', 'w') as f:
# #     f.write(str(dicEstudosPorDatas))
# #     f.close()
# # with open('FarmaPorCondicao.txt', 'w') as f:
# #     f.write(str(dicCondition))
# #     f.close()
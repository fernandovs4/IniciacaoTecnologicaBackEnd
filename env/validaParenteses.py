# import requests
# min_rank = 1
# max_rank = 1000
# query = {
#     'expr' : 'cancer and AREA[LeadSponsorClass]Industry',
#     'fields' : 'LeadSponsorClass,LeadSponsorName,LocationFacility, LocationCountry,StartDate',
#     'fmt' : 'JSON',   
#     'min_rnk' : min_rank,
#     'max_rnk' : max_rank
# }

# url = "http://ClinicalTrials.gov/api/query/study_fields"
# headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
# brasil = []
# i = 0 
# strin_dos_estudos = ''
# while True:
#     try:
#         response = requests.get(url, params=query) #, headers=headers)
#         print(i)
#         if response.status_code == 200:
#             # Request was successful, so parse the response data
        
#             data = response.json()
#             for estudo in data['StudyFieldsResponse']['StudyFields']:
#                 if 'Brazil' in estudo['LocationCountry']:
#                     strin_dos_estudos += str(estudo) + ','
#                     with open('arquivo4.txt', 'w') as f:
                
#                          f.write(str(strin_dos_estudos) )
          
            
            
            
#             # Do something with the data
#         else:
#             # Request failed, so handle the error
#             print("Error:", response.status_code)
#         min_rank += 100
#         max_rank += 100
#         i += 100
#     except:
#         strin_dos_estudos = "{" + strin_dos_estudos + "}"
#         with open('arquivo4.txt', 'w') as f:
                
#             f.write(str(strin_dos_estudos) )
          
#         break
# print("terminou")

import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font, Color, colors, Alignment
with open('f.txt', 'a') as f:
    wb = Workbook()
    ws = wb.active
    ws.title = "Estudos Farmacéuticos"
    ws["A1"] = "Pharmaceutical"
    ws['B1'] = 'A.C Camargo'
    ws['C1'] = 'Sírio Libanês'
    ws['D1'] = 'Albert Einstein'
    ws['E1'] = 'Moinhos de Vento'
    ws['F1'] = 'Beneficencia Portuguesa'
    hospitais = ['A.C Camargo', 'Sírio Libanês', 'Albert Einstein', 'Moinhos de Vento', 'Beneficencia Portuguesa']
    i = 2
    dicDeEstudos = {}
    estudos = eval(str(f))
    for farmaceutica in  estudos:
        if farmaceutica['LeadSponsorName'] not in dicDeEstudos:
            dicDeEstudos[farmaceutica['LeadSponsorName']] = { "A.C Camargo": 0, "Sírio Libanês": 0, "Albert Einstein": 0, "Moinhos de Vento": 0, "Beneficencia Portuguesa": 0}
        for hospital in hospitais:
            if hospital in farmaceutica['LocationFacility']:
                dicDeEstudos[farmaceutica['LeadSponsorName']][hospital] += 1
    for farma in dicDeEstudos.keys():
        ws['A' + str(i)] = farma
        ws['B' + str(i)] = dicDeEstudos[farma]['A.C Camargo']
        ws['C' + str(i)] = dicDeEstudos[farma]['Sírio Libanês']
        ws['D' + str(i)] = dicDeEstudos[farma]['Albert Einstein']
        ws['E' + str(i)] = dicDeEstudos[farma]['Moinhos de Vento']
        ws['F' + str(i)] = dicDeEstudos[farma]['Beneficencia Portuguesa']
        i += 1

    

    ws['A1'].font = Font(bold=True)
    ws['B1'].font = Font(bold=True)
    ws['C1'].font = Font(bold=True)
    ws['D1'].font = Font(bold=True)
    ws['E1'].font = Font(bold=True)
    ws['F1'].font = Font(bold=True)
    ws['A1'].alignment = Alignment(horizontal='center')
    ws['B1'].alignment = Alignment(horizontal='center')
    ws['C1'].alignment = Alignment(horizontal='center')
    ws['D1'].alignment = Alignment(horizontal='center')
    ws['E1'].alignment = Alignment(horizontal='center')
    ws['F1'].alignment = Alignment(horizontal='center')


    wb.save('arquivo4.xlsx')


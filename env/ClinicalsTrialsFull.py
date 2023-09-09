import requests


lista = []
i = 1
for i in range(0, 100, 100):
    try:
        resposta = requests.get(f"https://clinicaltrials.gov/api/query/full_studies?expr=cancer&min_rnk={i + 1}&max_rnk={99 + i}&fmt=json").json()
        
        lista.append(resposta)
        print(i)
        i+1
               
         
       
    except:
        print("erro")
        pass

print(lista)
with open("clinicalTrialsFull.txt", "w") as f:
    f.write(str(lista))
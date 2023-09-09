
import openai
import requests
import time
openai.organization = "org-76eQxbPcfiA1eR0yEknRqVe0"
openai.api_key = "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"


with open('todos_hospitais_por_linha.txt', 'r') as file:
    data = file.readlines()
    for hospital in data:
        b  = f"responda com um sim ou não se esse nome corresponde a uma empresa, faculdade, centro clínico ou hospital do brasil: {hospital}"
        l = b

        a = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"""{b}""",
        max_tokens=2048,

        temperature=0,
        echo = True,

        )['choices'][0]['text'].split(" ")[-1]



     
        with open ('resposta_do_chat.txt', 'a') as f:
            f.write(f"Hospital: {hospital} = " +  str(a)  +  "\n") 
            print(f"Hospital: {hospital} = " +  str(a)  +  "\n")
        time.sleep(1)




# import requests

# url = 'https://clinicaltrials.gov/ct2/results?cond=&term=&type=&rslt=&age_v=&gndr=&intr=&titles=&outc=&spons=&lead=&id=&cntry=BR&state=&city=&dist=&locn=&phase=4&phase=0&phase=1&phase=2&fund=2&rsub=&strd_s=&strd_e=&prcd_s=&prcd_e=&sfpd_s=&sfpd_e=&rfpd_s=&rfpd_e=&lupd_s=&lupd_e=&sort='
# response = requests.get(url)

# soup = BeautifulSoup(response.content, 'html.parser')

# lis = soup.find_all('li')


# print(lis)

# from serpapi import GoogleSearch
# lista = []
# with open('todos_hospitais_por_linha.txt', 'r') as file:
#     data = file.readlines()
#     for hospital  in data:
 

#         params = {
#         "engine": "duckduckgo",
#         "q": f"{hospital}",
#         "kl": "us-en",
#         "api_key": "398aa2a09fe7206cda848ffe7935bc86fedec5a1ba436c3e4f3b42a3434b7033"
#         }
#         try:

#             search = GoogleSearch(params)
#             results = search.get_dict()

#             with open('links_dos_hospitais.txt', 'a') as f:
#                 f.write(f"{hospital}: {results['organic_results'][0]['link']} \n")
#                 f.write(f"{hospital}: {results['organic_results'][1]['link']} \n")
#         except:
#             continue
            
       

#         print(results['organic_results'][0]['link'])



# from bs4 import BeautifulSoup
# import requests

# requisicao = requests.get('https://clinicaltrials.gov/ct2/results?cond=&term=&type=&rslt=&age_v=&gndr=&intr=&titles=&outc=&spons=&lead=&id=&cntry=BR&state=&city=&dist=&locn=&phase=4&phase=0&phase=1&phase=2&fund=2&rsub=&strd_s=&strd_e=&prcd_s=&prcd_e=&sfpd_s=&sfpd_e=&rfpd_s=&rfpd_e=&lupd_s=&lupd_e=&sort=')

# soup = BeautifulSoup(requisicao.content, 'html.parser')

# lis = soup.find_all('ul')
# for li in lis:
#     print(li.text)

from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()

driver.get('https://clinicaltrials.gov/ct2/results?cond=&term=&type=&rslt=&age_v=&gndr=&intr=&titles=&outc=&spons=&lead=&id=&cntry=BR&state=&city=&dist=&locn=&phase=4&phase=0&phase=1&phase=2&fund=2&rsub=&strd_s=&strd_e=&prcd_s=&prcd_e=&sfpd_s=&sfpd_e=&rfpd_s=&rfpd_e=&lupd_s=&lupd_e=&sort=')
time.sleep(2)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')


lis = soup.find_all('li')


for li in lis:
    print(li)

driver.quit()

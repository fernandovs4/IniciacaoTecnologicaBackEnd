



# import requests

# import json

# print(requests.get("https://kgsearch.googleapis.com/v1/entities:search?query=Sociedade&key=AIzaSyDd_bFLQRtnEOFKeyzNaBu8d5lNhMYIsck&limit=1&Place&indent=True").json())


# from googleapiclient.discovery import build
# import json

# api_key = 'AIzaSyDd_bFLQRtnEOFKeyzNaBu8d5lNhMYIsck'
# service_name = 'kgsearch'
# version = 'v1'

# service = build(service_name, version, developerKey=api_key)

# query = 'Centro de Investigacion Pergamino SA '

# response = service.entities().search(
#     query=query,
#     types=['Hospital'],
# ).execute()

# print(json.dumps(response, indent=2))

# from geopy.geocoders import Nominatim

# # Cria um objeto geolocalizador usando a API do OpenStreetMap
# geolocator = Nominatim(user_agent="my_app")

# # Exemplo de endereço de hospital
# endereco_hospital = "União Química Farmacêutica Nacional"

# # Obtem as coordenadas geográficas do endereço
# location = geolocator.geocode(endereco_hospital)

# # Obtem o nome do país em que o hospital está localizado
# pais = geolocator.reverse((location.latitude, location.longitude), exactly_one=True).raw['address']['country']

# # Verifica se o hospital está localizado no Brasil
# if pais == 'Brasil' or pais == 'Brasil':
#     print("O hospital está localizado no Brasil")
# else:
#     print("O hospital está localizado fora do Brasil")

import googlemaps

# Insira sua chave de API do Google Maps Places
gmaps = googlemaps.Client(key='AIzaSyDd_bFLQRtnEOFKeyzNaBu8d5lNhMYIsck')

# Exemplo de coordenadas geográficas
lat, lng = -23.550520, -46.633308  # São Paulo, Brasil

# Define os parâmetros da busca
params = {
    'location': (lat, lng),
    'radius': 5000,  # raio em metros
    'type': 'hospital'  # tipo de lugar
}

# Faz a busca na API do Google Maps Places
resultados = gmaps.places(**params)

# Filtra somente os hospitais do Brasil
hospitais_brasil = []
for resultado in resultados['results']:
    if 'formatted_address' in resultado:
        if 'Brazil' in resultado['formatted_address']:
            hospitais_brasil.append(resultado['name'])

# Exibe a lista de hospitais do Brasil encontrados
print(hospitais_brasil)



import json
import requests

def todos_hospitais():
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

    hospitais = []
    first_response = requests.get(url=url, params= query).json()
    NStudiesFound = first_response["StudyFieldsResponse"]["NStudiesFound"]

    while(query["max_rnk"] <= NStudiesFound):
        next_response = requests.get(url=url, params= query).json()
        study = next_response["StudyFieldsResponse"]["StudyFields"]
        hospitais += study
        query["min_rnk"] += 100
        query['max_rnk'] += 100


    return hospitais
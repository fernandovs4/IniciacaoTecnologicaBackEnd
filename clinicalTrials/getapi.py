import json
import requests
from pathlib import Path

PATH = Path(__file__).parent 
def todos_hospitais(cache = False, farmas = False):
    min_rank = 1
    max_rank = 100
    query = {
        'expr' : 'cancer AND  AREA[LeadSponsorClass]Industry AND SEARCH[Location](AREA[LocationCountry]Brasil)',
        'fields' : 'LeadSponsorClass,LeadSponsorName,LocationFacility,LocationCountry,OverallStatus,StdAge,StartDate,LocationZip,Gender,MaximumAge,MinimumAge,Condition,LocationState,WhyStopped,Phase',
        'fmt' : 'JSON',   
        'min_rnk' : min_rank,
        'max_rnk' : max_rank
    }
    cacheResults = {}
    url = "http://ClinicalTrials.gov/api/query/study_fields"

    if cache:
        with open(PATH / Path("json/cacheResults.json"), "r") as file:
            return json.load(file)

    hospitais = []
    first_response = requests.get(url=url, params= query).json()
    if cache:
        with open(PATH / Path("json/cacheResults.json"), "r") as file:
            cacheResults_ = json.load(file)
            if first_response["StudyFieldsResponse"]["DataVrs"] == cacheResults_["StudyFieldsResponse"]["DataVrs"]:
                return cacheResults_["StudyFieldsResponse"]["StudyFields"]
    LeadSponsorName = set()
            
    NStudiesFound = first_response["StudyFieldsResponse"]["NStudiesFound"]
    cacheResults["StudyFieldsResponse"] = {"DataVrs" : first_response["StudyFieldsResponse"]["DataVrs"], 
                                           "NStudiesAvail": first_response["StudyFieldsResponse"]["NStudiesAvail"], 
                                           "NStudiesFound": first_response["StudyFieldsResponse"]["NStudiesFound"], 
                                           "FieldList": first_response["StudyFieldsResponse"]["FieldList"], 
                                           "StudyFields": first_response["StudyFieldsResponse"]["StudyFields"]}


    for study in first_response["StudyFieldsResponse"]["StudyFields"]:
        print(study['LeadSponsorName'][0])
        
        LeadSponsorName.add(study['LeadSponsorName'][0])

    while(query["max_rnk"] <= NStudiesFound):
        next_response = requests.get(url=url, params= query).json()
        study = next_response["StudyFieldsResponse"]["StudyFields"]
        cacheResults["StudyFieldsResponse"]["StudyFields"] += study
        hospitais += study
        for study in next_response["StudyFieldsResponse"]["StudyFields"]:
           
            LeadSponsorName.add(study['LeadSponsorName'][0])
        query["min_rnk"] += 100
        query['max_rnk'] += 100
    LeadSponsorName = {"LeadSponsorName" : list(LeadSponsorName)}
    with open(PATH / Path("clinicalTrials/json/farmas.json"), "w") as file:
        json.dump(LeadSponsorName, file, indent=4)
    if farmas:
        return LeadSponsorName
    with open(PATH / Path("json/cacheResults.json"), "w") as file:
        json.dump(cacheResults, file, indent=4)

    return hospitais



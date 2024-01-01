import json
import requests
from pathlib import Path
from pprint import pprint
import time
PATH = Path(__file__).parent 
def todos_hospitais(cache = False, farmas = False):
    
    if cache:
            with open(PATH / Path("json/cacheResults.json"), "r") as file:
                return json.load(file)
    totalEstudos = 0
    expr = ["Neoplasms","Cancer","Tumors","Oncology"]
    LeadSponsorName = set()
    cacheResults = {"StudyFieldsResponse":{"StudyFields":[]}}
    i = 0
    cacheResults["StudyFieldsResponse"] = {"StudyFields": []}
    for tipo in expr:
        min_rank = 1
        max_rank = 1000
        query = {
            'expr' : f'{tipo} AND  AREA[LeadSponsorClass]Industry AND SEARCH[Location](AREA[LocationCountry]Brasil)',
            'fields' : 'LeadSponsorName,LocationFacility,LocationCountry,OverallStatus,StdAge,StartDate,Gender,MaximumAge,MinimumAge,Condition,LocationState,WhyStopped,Phase',
            'fmt' : 'JSON',   
            'min_rnk' : min_rank,
            'max_rnk' : max_rank
        }
        
        url = "http://ClinicalTrials.gov/api/query/study_fields"


    
        first_response = requests.get(url=url, params= query).json()
        # if cache:
        #     with open(PATH / Path("json/cacheResults.json"), "r") as file:
        #         cacheResults_ = json.load(file)
        #         if first_response["StudyFieldsResponse"]["DataVrs"] == cacheResults_["StudyFieldsResponse"]["DataVrs"]:
        #             return cacheResults_["StudyFieldsResponse"]["StudyFields"]
        
        NStudiesFound = first_response["StudyFieldsResponse"]["NStudiesFound"]
        
        try:
            for study in first_response["StudyFieldsResponse"]["StudyFields"]:
                LeadSponsorName.add(study['LeadSponsorName'][0])
        except:
            pass
        print(NStudiesFound)
    
        while query["max_rnk"] <= 1.5 * NStudiesFound:
            next_response = requests.get(url=url, params=query).json()
           
            try:
                study = next_response["StudyFieldsResponse"]["StudyFields"]
            except:

                print(tipo)
                
                print(query["min_rnk"])
                query["min_rnk"] += 1000
                query['max_rnk'] += 1000
                continue
            for std in study:
                std_sem_rank = std.copy()
                std_sem_rank.pop("Rank")
                if std_sem_rank  not in cacheResults["StudyFieldsResponse"]["StudyFields"]:
                    cacheResults["StudyFieldsResponse"]["StudyFields"].append(std_sem_rank)
                    totalEstudos += 1
                    print(i)                   
                    i += 1
                LeadSponsorName.add(std['LeadSponsorName'][0])            
            query["min_rnk"] += 1000
            query['max_rnk'] += 1000

    LeadSponsorName = {"LeadSponsorName" : list(LeadSponsorName)}
    with open(PATH / Path("json/farmas.json"), "w") as file:
        json.dump(LeadSponsorName, file, indent=4)
    if farmas:
        return LeadSponsorName
    cacheResults["StudyFieldsResponse"]["NStudiesFound"] = totalEstudos
    with open(PATH / Path("json/cacheResults.json"), "w") as file:
        json.dump(cacheResults, file, indent=4)
    
    return cacheResults


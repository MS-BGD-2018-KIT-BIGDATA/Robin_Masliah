import requests
import json
import pandas as pd


def getContent(url, headers=None):

    response = requests.get(url, headers=headers)
    return response.content


def get_drug(drug):

    result = []
    i =0
    while(True):
        i += 1
        url = 'https://www.open-medicaments.fr/api/v1/medicaments?query='+str(drug)+'&page='+str(i)+'&limit=50'
        response = getContent(url)
        list_drugs = json.loads(response)
        result.extend(getMedicament(list_drugs['codeCIS']) for drug in list_drugs)
    return result


def getMedicament(id):
    url = 'https://www.open-medicaments.fr/api/v1/medicaments/'+ str(id)

    medicament = {}

    response = getContent(url)
    infos = json.loads(response)
    
    medicament['id'] = infos['codeCIS']

    return medicament

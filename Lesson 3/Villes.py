import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


def get_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_distance(ville1, ville2):
    response = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins="+ville1+"&destinations="+ville2+"&key=AIzaSyBKED6FYbqdBZvufn-cYD--4MpyClWFrh4").json()
    data = response.json()
    print(type(data))
    print(response)
    return data["rows"][0]["elements"][0]["distance"]["text"]



def main():
# display some lines
    url = 'https://www.insee.fr/fr/statistiques/1906659'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    cities = soup.tbody.find_all(class_= 'ligne')
    cities_raw = [c.text.split(' ', 1)[0] for c in cities]
    print(cities_raw)
    
    ville1 = cities_raw[2]
    ville2 = cities_raw[4]
    
    get_distance(ville1, ville2)

if __name__ == "__main__": main()


# app_name/api.py
import requests
from .models import Country
"""
def fetch_country_data():
    url = 'https://countriesnow.space/api/v0.1/countries/capital'  # Replace with your API endpoint
    response = requests.get(url)
    data = response.json()

    for country in data:
        name = country['name']
        capital = country['capital']
        Country.objects.create(name=name, capital=capital)

"""
def fetch_country_data():
    url = 'https://countriesnow.space/api/v0.1/countries/capital'  # Replace with your API endpoint
    response = requests.get(url)
    data_1 = response.json()

    #key_objects = [(country['name'], country['capital']) for country in data_1['data']]  # Extracting name and capital as key objects
 


    #key_objects = [country['name'] for country in data_1['data']]  # Extracting name and capital as key objects

    key_objects = [country['name'] for country in data_1['data']]  # Extracting name and capital as key objects
    #key_objects_2 = [country['name'] +"-" + country['capital'] for country in data_1['data']] 

    print(type(key_objects))
    #print(key_objects, key_objects_2)
    #return key_objects, key_objects_2
    return key_objects



def check_capital_info(country_name, capital_name):
    url = 'https://countriesnow.space/api/v0.1/countries/capital'  # Replace with your API endpoint
    response = requests.get(url)
    data_1 = response.json()

    result = "NA"
    
    for country in data_1['data']:
        #print("country['name'] is : ", country['name'])
        if country['name'] == country_name:
            result=country['capital']
            
            #if country['capital'] == capital_name:
                #result = True
      
    return result

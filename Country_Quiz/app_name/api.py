# app_name/api.py
import requests
from .models import Country

def fetch_country_data():
    url = 'https://countriesnow.space/api/v0.1/countries/capital'  
    response = requests.get(url)
    data_1 = response.json()

    key_objects = [country['name'] for country in data_1['data']]  
    print(type(key_objects))
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

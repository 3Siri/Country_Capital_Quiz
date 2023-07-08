#from django.shortcuts import render

# Create your views here.

# app_name/views.py
from django.shortcuts import render, HttpResponse
from .models import Country
from .api import fetch_country_data, check_capital_info
from django.utils.safestring import mark_safe


def country_list(request):
    key_objects = fetch_country_data()
    return render(request, 'countries_list.html',{'key_objects': key_objects})

def check_capital(request):
    if request.method == 'GET':
        entered_capital = request.GET.get('capital')
        country_id = request.GET.get('country')

        print("entered_capital is : ", entered_capital)
        print("country_id is : ", country_id)
        
        actual_capital = check_capital_info(country_id, entered_capital)
        if actual_capital.lower() == entered_capital.lower():
            message = 'You have entered correct capital!'
        else:
            message = f'You have entered incorrect capital {entered_capital} and right capital is <strong>{actual_capital}</strong>.'
            message = mark_safe(message)


        return render(request, 'result.html', {'message': message})
    
    return HttpResponse('Invalid request method.')
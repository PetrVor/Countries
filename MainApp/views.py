from django.http import HttpResponse
from django.shortcuts import render
import json


with open('Countries.json') as file:
    countries = json.load(file) 
 

def home(request):
    return render(request,'home.html') 

def countries(request):
       with open('Countries.json') as file:
            countries = json.load(file) 
       context={            "countries" : countries       }
       file.close
       return render(request,'countries-list.html', context)

def get_country(request,country_name):

    with open('Countries.json') as file:
        countries = json.load(file)
    country = next((country for country in countries if country['country'] == country_name),None)
    if country is not None:
        context={"country": country}
        return render(request,'country.html', context)
    return HttpResponse(f"{country_name} is not found!")
    
def starts_letter(request,check):
    sorted_list = []
    with open('Countries.json') as file:
        countries = json.load(file)
    for country in countries:
        if country['country'][0].lower() == check.lower():
            sorted_list.append(country)
    context = {"countries": sorted_list}
    return render(request,"countries-list.html", context)

def starts(check):
    with open('Countries.json') as file:
        countries = json.load(file)
    sorted_list = []
    for country in countries:
        if country['country'][0].lower() == check.lower():
            sorted_list.append(country)
    return sorted_list    

def languages(request):
    languages=[]
    with open('Countries.json') as file:
        countries = json.load(file)
        for country in countries:
            for key,value in country.items():
                if key == 'languages':
                    for val in value:
                     if val not in languages:
                        languages.append(val)

        context={"languages" : languages}
    return render(request,'languages-list.html',context)

def get_lang(request,lang):
    countries_list=[]
    with open('Countries.json') as file:
        countries = json.load(file)
    for country in countries:
        for l in country['languages']:
            if l == lang and l not in countries_list:
                countries_list.append(country['country'])
    context ={"countries":countries_list}
    return render(request,'language.html',context)           
   

# lang = "Japanese"
# with open('Countries.json') as file:
#     countries = json.load(file)
#     for country in countries:
#         for l in country['languages']:
#             if l == lang:
#                 print(country['country'])
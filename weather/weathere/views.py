# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from weathere.models import regg
import requests,json

from weathere.forms import authform,regform
from django.shortcuts import render
from weathere.forms import authform
from django.contrib.auth import login,logout
# Create your views here.
def index(request):
    return render(request,'weathere/weath.html')
def main1(request):
    return render(request,'weathere/firstpage.html')

def contact(request):
    if(request.method=='POST'):
        print(request.POST)
        if(len(request.POST)==3):
            form=authform(request.POST)
            
            print(len(request.POST))
            if(form.is_valid()):
                userobj=form.cleaned_data
                #print(userobj['user'])
                #print(userobj['passer'])
        
                uname=request.POST.get('user')
                pass1=request.POST.get('passer')
                x=regg.objects.get(user=uname)
                print(x.passer)
                if(pass1==x.passer):
                    contents={
                        'condition':'Drizziling',
                        'city':'Chennai',
                        'temp':'90 F',
                        'mintemp':'75 F',
                        'maxtemp':'96 F',
                        'humidity':'200'
                        
                    }
                    return render(request,'weathere/mainpage.html',contents)
                else:
                    return render(request,'weathere/firstpage.html')
        else:
    
            reg=regform(request.POST)
            print(reg.is_valid())
            if(reg.is_valid()):
                regobj=reg.cleaned_data
                if(regobj['passer']==regobj['confpasser']):
                    event1=regg(user=regobj['user'],passer=regobj['passer'],confpasser=regobj['confpasser'],email=regobj['email'])
                    event1.save()
                    contents={
                        'condition':'Drizziling',
                        'city':'Chennai',
                        'temp':'90 F',
                        'mintemp':'75 F',
                        'maxtemp':'96 F'
                        
                    }
                    return render(request,'weathere/mainpage.html',contents)
                else:

                    return render(request,'weathere/register.html')  
       
def register(request):
    return render(request,'weathere/register.html')
    

def logout(request):
    if(request.method == "POST"):
        #logout(request)
        
        return render(request,'weathere/weath.html')           
def search(request):
    if(request.method=='POST'):
        contents={
            'condition':'Drizziling',
            'city':'Chennai',
            'temp':'90 F',
            'mintemp':'75 F',
            'maxtemp':'96 F',
            'country':'IN',
                        
        }       
        
        api="1dad01ac6312cd17e6117f4a18c5c6c4"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city=request.POST.get('city')
        complete_url = base_url + "appid=" + api + "&q=" + city
        response = requests.get(complete_url) 
        x=response.json()
        print(x)
        if(x['cod']!='404'):
            lon=x['coord']['lon']
            lat=x['coord']['lat']
            temp=x['main']['temp']-273.15
            max_temp=x['main']['temp_max']-273.15
            min_temp=x['main']['temp_min']-273.15
            condition=x['weather'][0]
            condition=condition['description'].capitalize()
            humidity=x['main']['humidity']
            pressure=x['main']['pressure']
            country=x['sys']['country']
            contents={
                'condition':condition,
                'city':city.capitalize(),
                'temp':temp,
                'mintemp':min_temp,
                'maxtemp':max_temp,
                'lat':lat,
                'lon':lon,
                'humidity':humidity,
                'country':country,
                        
            }
        return render(request,'weathere/mainpage.html',contents)            
        #print(lon,lat,temp,max_temp,min_temp,condition)
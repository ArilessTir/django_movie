from django.http import HttpResponse
from django.shortcuts import render

data ={
    'movies':[
    {'id':5,'title':'JAWS', 'year':1995},
    {'id':6,'title':'Sharknado', 'year':1985},
    {'id':7,'title':'Split', 'year':2012},
    {'id':8,'title':'LORD', 'year':2000},   
    ]
}

def movies(request):
    return render(request,'movies/movies.html',data)

def home(request):
    return HttpResponse('Home page')
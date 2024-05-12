from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse


def home(resquest):
    return HttpResponse('<h1>HOME </h1>')

def contato(resquest):
    return HttpResponse('<h1>HOME1 </h1>')

def sobre(resquest):
    return HttpResponse('<h1>HOME2 </h1>')
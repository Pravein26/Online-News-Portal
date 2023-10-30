from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def signup(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def news(request):
    template = loader.get_template('news.html')
    return HttpResponse(template.render())
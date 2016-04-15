from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
from .models import Greeting

# Create your views here.
def home(request):
    return render(request, 'home.html', {'greetings': greetings})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

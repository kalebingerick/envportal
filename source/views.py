from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
from source import templates
# Create your views here.
def home(request):
    return render(request, 'home.html')

from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
# Create your views here.
def home(request):
    return render(request, '../source/templates/home.html')

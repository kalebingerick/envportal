from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'envportal/home.html')
#enddef

def calendar(request):
    return render(request, 'envportal/calendar.html')
#enddef

@login_required(login_url='log_in')
def create_event(request):
  return render(request, 'envportal/create_event.html')
#enddef

@login_required(login_url='log_in')
def edit_event(request):
  return render(request, 'envportal/edit_events.html')

@login_required(login_url='log_in')
def user_dashboard(request):
	return render(request, 'envportal/user_dashboard.html')
	
def event_more_info(request):
    return render(request, 'envportal/event_more_info.html')
#enddef

def find_resources(request):
    return render(request, 'envportal/find_resources.html')
#enddef

def find_resources_search(request):
    return render(request, 'envportal/find_resources_search.html')
#enddef

def about(request):
    return render(request, 'envportal/about.html')
#enddef

def log_in(request):
    if request.method == "POST":
        username = 'john'
        password = 'password1234'
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/user_dashboard')
    return render(request, 'envportal/log_in.html')
#enddef

def sign_up(request):
    if request.method == "POST":
        try:
          u = User.objects.get(username='john')
        except User.DoesNotExist:
          u = None
        if u is None:
          u = User.objects.create_user('john', 'john.smith@gmail.com', 'password1234')
        return HttpResponseRedirect('/email_confirmation')
    return render(request, 'envportal/sign_up.html')
#enddef

def email_confirmation(request):
    return render(request, 'envportal/email_confirmation.html')


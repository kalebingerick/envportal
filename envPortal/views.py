from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'envportal/home.html')
#enddef

def calendar(request):
    return render(request, 'envportal/calendar.html')
#enddef

def create_event(request):
    return render(request, 'envportal/create_event.html')
#enddef

def event_more_info(request):
    return render(request, 'envportal/event_more_info.html')
#enddef

def find_resources(request):
    return render(request, 'envportal/find_resources.html')
#enddef

def log_in(request):
    return render(request, 'envportal/log_in.html')
#enddef

def sign_up(request):
    return render(request, 'envportal/sign_up.html')
#enddef
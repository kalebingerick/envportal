from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'envportal/home.html')
#enddef

def calendar(request):
    return render(request, 'envportal/calendar.html')
#enddef

def create_event(request):
	if request.user.is_authenticated():
		return render(request, 'envportal/create_event.html')
	else:
		need_auth(request)
		return render(request, 'envportal/create_event.html')
#enddef

def edit_event(request):
	if request.user.is_authenticated():
		return render(request, 'envportal/edit_events.html')
	else:
		need_auth(request)
		return render(request, 'envportal/edit_events.html')

def need_auth(request):
	log_in(request)
	return request
#enddef

def user_dashboard(request):
	return render(request, 'envportal/user_dashboard.html')
	
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
from django.conf.urls import url
from . import views

#app_name = 'envportal'

urlpatterns = [
	url(r'^home/$', views.home, name='home'),
	url(r'^calendar/$', views.calendar, name='calendar'),
	url(r'^create_event/$', views.create_event, name='create_event'),
	url(r'^event_more_info/$', views.create_event, name='event_more_info'),
	url(r'^find_resources/$', views.find_resources, name='find_resources'),
	url(r'^log_in/$', views.log_in, name='log_in'),
	url(r'^sign_up/$', views.sign_up, name='sign_up'),
]
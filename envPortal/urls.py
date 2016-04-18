from django.conf.urls import url
from django.contrib import admin
from . import views

#app_name = 'envportal'

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^about$', views.about, name='about'),
	url(r'^calendar$', views.calendar, name='calendar'),
    url(r'^create_event$', views.create_event, name='create_event'),
    url(r'^event_more_info$', views.create_event, name='event_more_info'),
    url(r'^find_resources$', views.find_resources, name='find_resources'),
	url(r'^find_resources_search$', views.find_resources_search, name='find_resources_search'),
    url(r'^log_in$', views.log_in, name='log_in'),
    url(r'^sign_up$', views.sign_up, name='sign_up'),
    url(r'^user_dashboard$', views.user_dashboard, name='user_dashboard'),
    url(r'^edit_event$', views.edit_event, name='edit_event'),
    url(r'^email_confirmation$', views.email_confirmation, name='email_confirmation'),
]

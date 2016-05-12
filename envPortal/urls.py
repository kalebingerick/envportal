from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

#app_name = 'envportal'

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^about$', views.about, name='about'),
    url(r'^attending$', views.attending, name='attending'),
	url(r'^calendar$', views.calendar, name='calendar'),
    url(r'^create_event$', views.create_event, name='create_event'),
    url(r'^event_more_info$', views.event_more_info, name='event_more_info'),
    url(r'^find_resources$', views.find_resources, name='find_resources'),
	url(r'^find_resources_search$', views.find_resources_search, name='find_resources_search'),
    url(r'^log_in$', views.log_in, name='log_in'),
    url(r'^sign_up$', views.sign_up, name='sign_up'),
    url(r'^user_dashboard$', views.user_dashboard, name='user_dashboard'),
    url(r'^edit_event$', views.edit_event, name='edit_event'),
    url(r'^email_confirmation$', views.email_confirmation, name='email_confirmation'),
	url(r'^rsvp_confirmation$', views.rsvp_confirmation, name='rsvp_confirmation'),
  url(r'^events/oil_bill/$', TemplateView.as_view(template_name='envportal/events/oil_bill.html'), name="oil_bill"),
  url(r'^events/trash_pickup/$', TemplateView.as_view(template_name='envportal/events/trash_pickup.html'), name="trash_pickup"),
  url(r'^events/tree_planting/$', TemplateView.as_view(template_name='envportal/events/tree_planting.html'), name="tree_planting"),
  url(r'^events/volunteer/$', TemplateView.as_view(template_name='envportal/events/volunteer.html'), name="volunteer"),
  url(r'^resources/green_earth/$', TemplateView.as_view(template_name='envportal/resources/green_earth.html'), name="green_earth"),
  url(r'^resources/trash_into_treasure/$', TemplateView.as_view(template_name='envportal/resources/trash_into_treasure.html'), name="trash_into_treasure"),
  url(r'^resources/better_than_dirt/$', TemplateView.as_view(template_name='envportal/resources/better_than_dirt.html'), name="better_than_dirt"),
  url(r'^resources/can_collection/$', TemplateView.as_view(template_name='envportal/resources/can_collection.html'), name="can_collection"),
  url(r'^resources/timber/$', TemplateView.as_view(template_name='envportal/resources/timber.html'), name="timber"),
  url(r'^resources/jeans_and_jackets/$', TemplateView.as_view(template_name='envportal/resources/jeans_and_jackets.html'), name="jeans_and_jackets"),
  url(r'^resources/volunteer_center/$', TemplateView.as_view(template_name='envportal/resources/volunteer_center.html'), name="volunteer_center"),
]

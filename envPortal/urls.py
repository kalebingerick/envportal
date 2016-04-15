from django.conf.urls import url
from . import views

app_name = 'envportal'

urlpatterns = [
	url(r'^home/$', views.home)
]
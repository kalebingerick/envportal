"""uxexperience URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from envPortal import views

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^calendar$', views.calendar, name='calendar'),
    url(r'^create_event$', views.create_event, name='create_event'),
    url(r'^event_more_info$', views.create_event, name='event_more_info'),
    url(r'^find_resources$', views.find_resources, name='find_resources'),
    url(r'^log_in$', views.log_in, name='log_in'),
    url(r'^sign_up$', views.sign_up, name='sign_up'),
    url(r'^user_dashboard$', views.user_dashboard, name='user_dashboard'),
    url(r'^edit_event$', views.edit_event, name='edit_event'),
    url(r'^email_confirmation$', views.email_confirmation, name='email_confirmation'),
]

from django.conf.urls import url
<<<<<<< HEAD
from django.contrib import admin
import envTest.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^home/', envTest.views.home, name='home'),
]
=======
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
>>>>>>> origin/django_fix

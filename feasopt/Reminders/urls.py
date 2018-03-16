from django.conf.urls import url

from . import views

app_name = 'reminders'

urlpatterns = [

    url(r'^$', views.reminders, name='reminders'),
]
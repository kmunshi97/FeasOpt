from django.conf.urls import url

from . import views

app_name = 'globals'

urlpatterns = [

    url(r'^$', views.globals, name='login'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
]
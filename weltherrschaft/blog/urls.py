from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    
)

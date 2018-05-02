from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from .views import *

app_name='directory'
urlpatterns = [
   # url(r'^sortby=(?P<sorting_string>[-a-z&_]+)$',index, name='index'),
    url(r'^page=(?P<page>\d+)$',index, name='index'),
    url(r'^sortby=(?P<sorting_string>-?name)(&page=(?P<page>\d+))?$',index, name='index'),
    url(r'^sortby=(?P<sorting_string>-?industries)(&page=(?P<page>\d+))?$',index, name='index'),
    url(r'^sortby=(?P<sorting_string>-?year_founded)(&page=(?P<page>\d+))?$',index, name='index'),
    url(r'^sortby=(?P<sorting_string>-?stage)(&page=(?P<page>\d+))?$',index, name='index'),
    url(r'^sortby=(?P<sorting_string>-?funding)(&page=(?P<page>\d+))?$',index, name='index'),
    url(r'^profile/(?P<company_id>\d+)$', profile, name='profile'),
    url(r'^(?P<field>\w+)=(?P<category>[\w -]+)',show_category, name='show_category'),
    url(r'^filter',filter, name='filter'),
    url(r'^$',home, name='home'),
]

from django.conf.urls import url
from django.conf.urls.static import static
from .views import *

app_name='directory'
urlpatterns = [
    url(r'^$(?P<sorting_string>)$',index, name='home'),
   # url(r'^sortby=(?P<sorting_string>[-a-z&_]+)$',index, name='index'),
    url(r'^sortby=(?P<sorting_string>-?name)$',index, name='index'),
    url(r'^sortby=(?P<sorting_string>-?industries)$',index, name='index'),
    url(r'^sortby=(?P<sorting_string>-?year_founded)$',index, name='index'),
    url(r'^sortby=(?P<sorting_string>-?stage)$',index, name='index'),
    url(r'^sortby=(?P<sorting_string>-?funding)$',index, name='index'),
    url('^profile/(?P<company_id>\d+)$', profile),
]

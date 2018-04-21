from django.conf.urls import url
from django.conf.urls.static import static
from .views import *

app_name='directory'
urlpatterns = [
    url(r'^$(?P<sorting_string>)$',index, name='home'),
    url(r'^sortby=(?P<sorting_string>[a-z&-_]+)$',index, name='index'),
    url(r'^search=(?P<searched_string>)$', search),
    url('^profile/(?P<company_id>\d+)$', profile),
]

from django.conf.urls import url
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    url(r'^$(?P<sortby>)$',index),
    url(r'^sortby=(?P<sortby>)$',index),
    url(r'^search=(?P<searched_string>)$', search),
    url('^profile/(?P<company_id>\d+)$', profile),
]

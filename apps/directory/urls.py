from django.conf.urls import url
from django.conf.urls.static import static
from .views import index, profile

urlpatterns = [
    url(r'^$',index),
    url(r'^sortby=(?P<sortby>)$',index),
    url(r'^search=(?P<searched_string>)$', search),
    url('^(?P<company_id>\d+)$', profile),
]

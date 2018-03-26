from django.conf.urls import url
from django.conf.urls.static import static
from .views import index, profile

urlpatterns = [
    url(r'^$',index,name='index'),
    url('^(?P<comapany_id>\d+)$',profile,name='profile'),
]

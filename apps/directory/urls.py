from django.conf.urls import url, path

from .views import index
B

urlpatterns = [
    url(r'',index,name='index'),
    path('<int:comapany_id/',profile,name='profile'),
]

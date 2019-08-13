from django.conf.urls import url
from . import views

urlpatterns = [

    url('^$', views.Index.as_view(), name='index'),
    url('distance.html', views.distance, name='distance')

]
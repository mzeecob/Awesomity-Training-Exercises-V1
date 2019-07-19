from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.UserFormView.as_view(), name='index'),

]

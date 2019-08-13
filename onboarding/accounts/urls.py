from django.conf.urls import url
from . import views

urlpatterns = [

    url('^$', views.index, name='index'),
    url('accounts/register/$', views.UserFormView.as_view(), name='register'),
    url('accounts/login/$', views.LoginFormView.as_view(), name='home'),
]
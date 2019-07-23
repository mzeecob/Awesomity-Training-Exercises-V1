from django.conf.urls import url
from . import views

urlpatterns = [
    # url('^$', views.index, name='index'),
    url('^$', views.LoginFormView.as_view(), name='login'),
    url('register.html/$', views.UserFormView.as_view(), name='register'),
    url('home.html/', views.index, name='home'),
    url('login.html/$', views.LoginFormView.as_view(), name='home'),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^login/$', views.user_login, name='login'),
    url('login/register.html', views.UserFormView.as_view(), name='register'),
]

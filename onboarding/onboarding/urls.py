from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('register.urls')),
    path('upload/', include('upload.urls')),
    path('map/', include('map.urls')),

]

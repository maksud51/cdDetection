from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',include('yoloapp.urls')),
    path('admin/', admin.site.urls),
]

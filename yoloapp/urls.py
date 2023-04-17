from django.urls import path
from .views import DETECTION
urlpatterns = [path('',DETECTION.as_view())]


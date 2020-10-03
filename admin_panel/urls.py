from django.urls import path
from .views import admin


urlpatterns = [
    path('dashboard/',admin , name='admin'),
]

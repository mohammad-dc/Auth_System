from django.urls import path, include
from app import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]

from django.urls import path
from foods.views import home

urlpatterns = [
    path('', home)
]

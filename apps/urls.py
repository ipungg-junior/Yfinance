from django.urls import path
from apps.views import *

urlpatterns = [
    path('', Landing.main)
]

from django.conf import settings
from django.urls import path, include
from .views import *

urlpatterns = [
    path('service/', ServiceView.as_view()),
]
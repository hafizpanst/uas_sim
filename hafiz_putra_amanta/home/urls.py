from django.urls import path
from home.views import *

urlpatterns = [
    path("", home_view),
    path("404", error_view),
]

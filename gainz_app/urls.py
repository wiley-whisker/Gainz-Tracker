from django.urls import path

from .views import *


urlpatterns = [
    path('', home, name='gainz_home'),
]

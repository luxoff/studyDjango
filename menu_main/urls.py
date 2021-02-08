from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>', menuItem_info),
    path('addcat/', add_category)
]
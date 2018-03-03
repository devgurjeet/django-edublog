from django.urls import path, include
from .views import *

urlpatterns = [
    path(r'', home, name='home'),
    path(r'list/', list, name='list'),
    path(r'details/<int:id>/', details, name='details'),
]
from django.urls import path
from .views import *


urlpatterns = [
    path('date/<int:year>/', TestIndexView.as_view())
]
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index),
    path('page', views.page),
    path('page2', views.page2),
]
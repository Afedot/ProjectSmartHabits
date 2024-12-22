from . import views
from django.urls import path, include
from .views import login_view, home_view
from .views import index, login_view

# urlpatterns = [
#     path('', index, name='index'),
#     path('login/', login_view, name='login'),
# ]


urlpatterns = [
    path('', index, name='index'),
    path('page', views.page),
    path('page2', views.page2),
    path('page3', views.page3),
]
# var_routing/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # /var_routing/
    path('', views.index),
    # /var_routing/greeting/유태영/
    path('greeting/<str:name>/', views.greeting),

    # /var_routing/cube/3/ 
    path('cube/<int:num>/', views.cube),

]

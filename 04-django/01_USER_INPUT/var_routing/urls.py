# var_routing/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # /var_routing/
    path('', views.index),
    # /var_routing/greeting/유태영/
    path('greeting/name/', views.greeting),

    # /var_routing/no/2023/ 

]

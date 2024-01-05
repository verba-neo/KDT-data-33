# home/urls.py (새로만들기)

from django.urls import path
from . import views

# 반드시 변수명 urlpatterns
urlpatterns = [
    # /home/test/
    path('test/', views.test),
    # /home/
    path('', views.index),
    # /home/about/
    # /home/contact/
]
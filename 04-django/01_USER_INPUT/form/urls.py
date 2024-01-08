from django.urls import path
from . import views

urlpatterns = [
    # /form/ping/
    path('ping/', views.ping),
    # /form/pong/
    path('pong/', views.pong),
]

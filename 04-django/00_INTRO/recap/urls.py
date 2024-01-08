from django.urls import path
from . import views

# urlpatterns 변수명은 고정
urlpatterns = [
    # /recap/
    path('', views.index),
    # /recap/is_xmas/
    path('is_xmas/', views.is_xmas),
    # /recap/lunch/
    path('lunch/', views.lunch)
]
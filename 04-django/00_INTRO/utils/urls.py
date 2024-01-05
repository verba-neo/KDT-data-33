from django.urls import path
from . import views


urlpatterns = [
    # utils/lotto/
    path('lotto/', views.lotto),
    # utils/kospi/
    path('kospi/', views.kospi),
]
from django.urls import path
from . import views

urlpatterns = [
    # board/new/
    path('new/', views.new),
    # board/create/
    path('create/', views.create),
]

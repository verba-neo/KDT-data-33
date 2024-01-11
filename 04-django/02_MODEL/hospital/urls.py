from django.urls import path
from . import views

app_name = 'hospital'

urlpatterns = [
    # /hospital/new/
    path('new/', views.new, name='new'),
    # /hospital/create/
    path('create/', views.create, name='create'),
    # /hospital/
    path('', views.index, name='index'),
    # /hospital/1/
    path('<int:pk>/', views.detail, name='detail'),
    # /hospital/1/edit/
    path('<int:pk>/edit/', views.edit, name='edit'),
    # /hospital/1/update/
    path('<int:pk>/update/', views.update, name='update'),
    # /hospital/1/delete/
    path('<int:pk>/delete/', views.delete, name='delete'),
    
]

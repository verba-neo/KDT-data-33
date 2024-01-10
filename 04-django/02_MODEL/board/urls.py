from django.urls import path
from . import views

urlpatterns = [
# Create
    # board/new/ => 게시글 작성용 <form> 제공
    path('new/', views.new),
    # board/create/ => 게시글 DB에 저장
    path('create/', views.create),
# Read
    # board/ => 전체 게시글 목록 조회
    path('', views.index),
    # board/1/ => 특정(pk)게시글 상세 조회
    path('<int:pk>/', views.detail),
]

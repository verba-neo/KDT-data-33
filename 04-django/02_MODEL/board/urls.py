# board/urls.py
from django.urls import path
from . import views

# URL을 쓸 일이 있으면, '<app_name>:<name>'
app_name = 'board'

urlpatterns = [
# Create
    # board/create/ => HTML / DB에 저장
    path('create/', views.create, name='create'),
# Read
    # board/ => 전체 게시글 목록 조회
    path('', views.index, name='index'),
    # board/1/ => 특정(pk)게시글 상세 조회 => 'board:detail'
    path('<int:pk>/', views.detail, name='detail'),
# Update
    # board/1/update/ => 수정된 게시글을 DB에 저장
    path('<int:pk>/update/', views.update, name='update'),
# Delete
    # board/1/delete/ => 특정(pk)게시글 삭제
    path('<int:pk>/delete/', views.delete, name='delete'),
]

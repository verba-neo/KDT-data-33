from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # board/create/
    path('create/', views.article_create, name='article_create'),
    # board/
    path('', views.article_index, name='article_index'),
    # board/1/
    path('<int:article_pk>/', views.article_detail, name='article_detail'),
    # board/1/update/
    path('<int:article_pk>/update/', views.article_update, name='article_update'),
    # board/1/delete/
    path('<int:article_pk>/delete/', views.article_delete, name='article_delete'),
    # board/1/comments/create/
    path('<int:article_pk>/comments/create/', views.comment_create, name='comment_create'),
    # board/1/comments/1/delete/
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    # board/1/like/
    path('<int:article_pk>/like/', views.article_like, name='article_like'),
]

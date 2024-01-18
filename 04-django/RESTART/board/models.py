from django.db import models
from django.conf import settings

class Article(models.Model):
    # models.py 한정>
        # 다른 모델들과 달리, User 를 관계로 설정할 때에는 모델명을 settings.AUTH_USER_MODEL 로 적는걸 권장.
        # 'User' 나 get_user_model() 은 권장하지 않음.
    
    # User : Article = 1 : N => 작성자
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # User : Article = M : N => 좋아요
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    # dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_articles')

    title = models.CharField(max_length=200)
    content = models.TextField()
    # timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    content = models.CharField(max_length=300)
    # timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    
    # article.comment_set.all() => 게시글이 가지고 있는 모든 댓글들 조회


class Comment(models.Model):
    # FK (외래키) => Article 모델 참조 / Article 삭제시 참조하는 댓글도 모두 삭제
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

    # comment.article => 댓글의 원 게시글 조회

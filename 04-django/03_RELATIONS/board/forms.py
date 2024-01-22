from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        # 아래 필드들은 안쓰겠다.
        exclude = ('user', )

        # 아래 필드들을 쓰겠다.
        # fields = ('title', 'content',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', )
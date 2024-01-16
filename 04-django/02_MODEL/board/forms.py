from django import forms
from .models import Article, Comment

# ModelForm => 특정 모델과 연동되는 Form
# 사용자 입력 HTML (input/textarea/..)을 생성
# 입력 데이터 검증(Validation) => 저장까지도 대신 해줌
class ArticleForm(forms.ModelForm):
    # forms.CharField => DB 컬럼 X / 문자열을 받겠다 O
    title = forms.CharField(min_length=2, max_length=100)
    content = forms.CharField(
        min_length=5,
        # forms.CharField 는 기본적으로 <input type="text"> 생성
        # widget을 통해서 HTML 코드를 바꿀 수 있음
        widget=forms.Textarea(
            # HTML class 주는 예시
            attrs={'class': 'my-class'}
        )
    )

    # python metaclass X / django 에서 추가정보를 표시하는 방법
    class Meta:
        # Article 모델과 연동
        model = Article
        # 아래에 입력된 필드에 대해서만 검증 
        fields = '__all__'


class CommentForm(forms.ModelForm):

    content = forms.CharField(min_length=2, max_length=100)

    class Meta:
        model = Comment
        fiedls = '__all__'
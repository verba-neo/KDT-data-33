from django.shortcuts import render
from .models import Article

def new(request):
    return render(request, 'board/new.html')


def create(request):
    article = Article()
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
    # 사용자에게 어떤 응답을 해줄지 고민


def index(request):
    articles = Article.objects.all()
    return render(request, 'board/index.html', {
        'articles': articles,
    })


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'board/detail.html', {
        'article': article,
    })

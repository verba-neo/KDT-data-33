from django.shortcuts import render, redirect
from .models import Article

# 생성
def new(request):
    return render(request, 'board/new.html')


def create(request):
    article = Article()
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
    # 저장 후 상세보기로 redirect
    return redirect('board:detail', article.pk)


# 조회
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


# 수정
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'board/edit.html', {
        'article': article,
    })


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
    # 저장 후 상세보기로 redirect
    return redirect('board:detail', article.pk)

# 삭제
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('board:index')

from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# 생성
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('board:detail', article.pk)
        
    elif request.method == 'GET':
        form = ArticleForm()

    return render(request, 'board/new.html', {'form': form })


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
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('board:detail', article.pk)
    
    elif request.method == 'GET':
        form = ArticleForm(instance=article)

    return render(request, 'board/edit.html', {
        'form': form,
    })


# 삭제
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('board:index')

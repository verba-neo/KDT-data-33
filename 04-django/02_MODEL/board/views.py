from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# 생성
def new(request):
    form = ArticleForm()
    return render(request, 'board/new.html', {
        'form': form,
    })


def create(request):
    # 넘어온 데이터를 통째로 form 에 입력
    form = ArticleForm(request.POST)
    # form 이 유효하다면,
    if form.is_valid():
        # form을 통해 article instance 저장
        article = form.save()
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

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
    # 유효하지 않다면
    else:
        # 사용자 입력 데이터 + 에러 메시지를 다시 new.html 에서 보여줌
        return render(request, 'board/new.html', {
            'form': form,
        })


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
    form = ArticleForm(instance=article)
    return render(request, 'board/edit.html', {
        'article': article,
        'form': form,
    })


def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 사용자 데이터와 기존 article 을 같이 활용해야함!
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        article = form.save()
        return redirect('board:detail', article.pk)
    else:
        return render(request, 'board/edit.html', {
            'article': article,
            'form': form,
        })

# 삭제
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('board:index')

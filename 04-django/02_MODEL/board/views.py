from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_POST

from .models import Article, Comment
from .forms import ArticleForm, CommentForm


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('board:detail', article.pk)
        
    elif request.method == 'GET':
        form = ArticleForm()

    return render(request, 'board/new.html', {'form': form })


@require_safe
def index(request):
    articles = Article.objects.all()
    return render(request, 'board/index.html', {
        'articles': articles,
    })


@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm()
    return render(request, 'board/detail.html', {
        'article': article,
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
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


@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('board:index')



# HTML(<form>) 은 article detail 에서 제공
# 여기서는 검증 => 저장만 진행
def create_comment(request, pk):  # board/1/comments/create/
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(request.POST)
    
    if form.is_valid():
        # comment 인스턴스에 내용을 채우되, 저장 직전에서 멈춰라
        comment = form.save(commit=False)
        # 댓글이 달린 게시글 지정
        comment.article = article
        comment.save()

    return redirect('board:detail', pk)


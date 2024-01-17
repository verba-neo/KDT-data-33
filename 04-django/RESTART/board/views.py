from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods

from .models import Article, Comment
from .forms import ArticleForm, CommentForm


@require_http_methods(['GET', 'POST'])
def article_create(request):
    # POST => 데이터 저장하기
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('board:article_detail', article.pk)
            
    # GET => 화면(html form>주기
    elif request.method == 'GET':
        form = ArticleForm()

    return render(request, 'board/form.html', {
        'form': form,
    })


@require_safe
def article_index(request):
    # 최신글(pk 큰것)부터 보여주기
    articles = Article.objects.order_by('-pk')
    return render(request, 'board/index.html', {
        'articles': articles,
    })


@require_safe
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # comment create 를 위한 form
    form = CommentForm()
    return render(request, 'board/detail.html', {
        'article': article,
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def article_update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    # POST => 데이터 저장하기
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('board:article_detail', article.pk)
            
    # GET => 화면(html form)주기
    elif request.method == 'GET':
        form = ArticleForm(instance=article)

    return render(request, 'board/form.html', {
        'form': form,
    })


@require_POST
def article_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('board:article_index')


@require_POST
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        # 저장 직전에 멈춰!
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
    # 저장과 상관없이 마지막엔 redirect        
    return redirect('board:article_detail', article.pk)


@require_POST
def comment_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('board:article_detail', article.pk)

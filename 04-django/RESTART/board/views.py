from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required

from .models import Article, Comment
from .forms import ArticleForm, CommentForm


@login_required
@require_http_methods(['GET', 'POST'])
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('board:article_detail', article.pk)
            
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


@login_required
@require_http_methods(['GET', 'POST'])
def article_update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    # '지금 요청 보낸 너'가 글쓴이가 아니라면
    if request.user != article.user:
        return redirect('board:article_detail', article.pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            # 이미 처음 생성될 때, article.user 가 들어감. 
            article = form.save()
            return redirect('board:article_detail', article.pk)            
    elif request.method == 'GET':
        form = ArticleForm(instance=article)

    return render(request, 'board/form.html', {
        'form': form,
    })


@login_required
@require_POST
def article_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.user != article.user:
        return redirect('board:article_detail', article.pk)

    article.delete()
    return redirect('board:article_index')


@login_required
@require_POST
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        # 저장 직전에 멈춰!
        comment = form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    # 저장과 상관없이 마지막엔 redirect        
    return redirect('board:article_detail', article.pk)


@login_required
@require_POST
def comment_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user != comment.user:
        return redirect('board:article_detail', article.pk)

    comment.delete()
    return redirect('board:article_detail', article.pk)

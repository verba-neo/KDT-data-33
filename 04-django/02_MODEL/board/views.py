from django.shortcuts import render
from .models import Article

def new(request):
    return render(request, 'board/new.html')


def create(request):
    article = Article()
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
# home/views.py
from django.shortcuts import render
from django.http import HttpResponse


def test(request):
    # django는 템플릿(html)을 찾을때, 
    # 자동으로 templates/ 폴더를 찾는다!
    return render(request, 'test.html')


def index(request):
    return render(request, 'index.html')





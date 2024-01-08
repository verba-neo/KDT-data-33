# var_routing/views.py

from django.shortcuts import render


def index(request):
    return render(request, 'var_routing/index.html')


def greeting(request):
    return render(request, 'var_routing/greeting.html')

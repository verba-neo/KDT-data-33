"""
URL configuration for intro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


def test(request):
    from django.http import HttpResponse
    print('test 함수가 실행되었습니다!!!')
    return HttpResponse('hi!')


def home(request):
    from django.http import HttpResponse
    return HttpResponse('This is Home page')


urlpatterns = [
    # 127.0.0.1:8000/test/
    path('test/', test),

    # 127.0.0.1:8000/
    path('', home)
]

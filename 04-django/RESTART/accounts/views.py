from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # 회원 등록
            user = form.save()
            # 바로 이어서 로그인 시켜주기
            auth_login(request, user)
            return redirect('board:article_index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        # AuthenticationForm 은 다른 ModelForm 들과는 다르다! 
        form = AuthenticationForm(request, data=request.POST)
        # id/pw 가 맞다면
        if form.is_valid():
            # 해당 사용자를 조회해서 return
            user = form.get_user()
            # 로그인 시켜주기
            auth_login(request, user)
            return redirect('board:article_index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {
        'form': form,
    })


def logout(request):
    pass
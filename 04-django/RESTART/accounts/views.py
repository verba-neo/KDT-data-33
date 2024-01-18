from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_safe
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import get_user_model


@require_http_methods(['GET', 'POST'])
def signup(request):
    # 만약 사용자가 로그인한 상태라면
    if request.user.is_authenticated:
        return redirect('board:article_index')

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
    # 만약 사용자가 로그인한 상태라면
    if request.user.is_authenticated:
        return redirect('board:article_index')

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
    auth_logout(request)
    return redirect('board:article_index')


@require_safe
def profile(request, username):
    # 사용자 단일 상세 조회
    user = get_object_or_404(get_user_model(), username=username)
    return render(request, 'accounts/profile.html', {
        'user': user,
    })
    
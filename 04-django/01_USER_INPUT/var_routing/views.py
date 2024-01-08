# var_routing/views.py

from django.shortcuts import render


def index(request):
    return render(request, 'var_routing/index.html')


# variable routing 에서 사용한 변수명을
# view 함수의 parameter 이름과 똑같이 설정해야함.
def greeting(request, name):
    return render(request, 'var_routing/greeting.html', {
        'name': name,
    })


def cube(request, num):
    answer = num ** 3
    return render(request, 'var_routing/cube.html', {
        'answer': answer,
    })

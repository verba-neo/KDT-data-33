from django.shortcuts import render


def ping(request):
    # <form> 담긴 HTML 을 넘겨준다.
    return render(request, 'form/ping.html')


def pong(request):
    x = request.GET['qwer']
    y = request.GET['asdf']

    print(x, y)

    return render(request, 'form/pong.html')

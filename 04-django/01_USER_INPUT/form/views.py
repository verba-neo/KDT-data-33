from django.shortcuts import render


def ping(request):
    # <form> 담긴 HTML 을 넘겨준다.
    return render(request, 'form/ping.html')


def pong(request):
    title = request.GET['title']
    content = request.GET['content']

    return render(request, 'form/pong.html', {
        'title': title,
        'content': content,
    })

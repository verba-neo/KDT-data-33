from django.shortcuts import render
from datetime import datetime
import random

def index(request):
    return render(request, 'recap/index.html')


def is_xmas(request):
    today = datetime.now()
    if today.month == 12 and today.day == 25:
        result = 'Yes'
    else:
        result = 'No'

    return render(request, 'recap/is_xmas.html', {
        'result': result,
    })


def lunch(request):
    menus = ['짜장면', '백반', '샐러드', 
            '순대국', '샌드위치', '떡볶이',]
    
    menu = random.choice(menus)

    return render(request, 'recap/lunch.html', {
        'menu': menu,
    })



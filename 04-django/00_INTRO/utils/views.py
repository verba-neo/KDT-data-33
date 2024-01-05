from django.shortcuts import render
import random


def lotto(request):
    lotto_numbers = random.sample(range(1, 46), 6)
    lotto_numbers.sort()
    
    return render(request, 'lotto.html', {
        'lotto_numbers': lotto_numbers,
    })


def kospi(request):
    return render(request, 'kospi.html')
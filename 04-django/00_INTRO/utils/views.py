from django.shortcuts import render
import random

import requests
from bs4 import BeautifulSoup

def lotto(request):
    lotto_numbers = random.sample(range(1, 46), 6)
    lotto_numbers.sort()

    return render(request, 'lotto.html', {
        'lotto_numbers': lotto_numbers,
    })



def kospi(request):
    URL = 'https://finance.naver.com/sise'
    res = requests.get(URL)
    doc = BeautifulSoup(res.text, 'html.parser')
    kospi = doc.select_one('#KOSPI_now').text

    return render(request, 'kospi.html', {
        'kospi': kospi,
    })
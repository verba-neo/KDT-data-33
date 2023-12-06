# kospi.py
import requests
from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/sise/'

# naver 증권에 접속하여 전체 페이지를 다운받는다.
page = requests.get(URL)

# Parsing (구문분석/해석)
data = BeautifulSoup(page.text, 'html.parser')

# KOSPI 현재 지수 데이터를 찾아 낸다.
kospi = data.select_one('#KOSPI_now')

# 찾은 데이터를 출력한다.
print(kospi.text)

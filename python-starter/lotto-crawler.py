# lotto-crawler.py

import requests
from bs4 import BeautifulSoup

URL = 'https://dhlottery.co.kr/common.do?method=main'


# 동행복권에 접속하여 전체 페이지를 다운받는다.
page = requests.get(URL)
# Parsing 작업을 한다.
data = BeautifulSoup(page.text, 'html.parser')

# 내가 원하는 데이터를 찾아 낸다.
# 1. 1등 총 당첨금(금액만)
first = data.select_one('#winnerId > dl > dd > strong')
print(first.text)

# 2. 숫자 6개
ball1 = data.select_one('#drwtNo1').text
ball2 = data.select_one('#drwtNo2').text
ball3 = data.select_one('#drwtNo3').text
ball4 = data.select_one('#drwtNo4').text
ball5 = data.select_one('#drwtNo5').text
ball6 = data.select_one('#drwtNo6').text

print(ball1, ball2, ball3, ball4, ball5, ball6)
# 3. 보너스 번호
bonus = data.select_one('#bnusNo').text
print(bonus)

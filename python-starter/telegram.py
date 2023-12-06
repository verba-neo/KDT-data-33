# telegram.py
import requests
from bs4 import BeautifulSoup
# Bot 정보
TOKEN = '<TOKEN>'
# 내 정보
MY_ID = '<ID>'

# 아래 URL 로 접속시 지금까지 bot이 받은 메시지들 확인 가능
'https://api.telegram.org/bot<token>/getUpdates'

TELEGRAM_URL = 'https://api.telegram.org/<TOKEN>/sendMessage?chat_id=<ID>&text='

SHOP_URL = 'https://search.shopping.naver.com/search/all?adQuery=rtx%204070ti&catId=50003104&frm=NVSHATC&origQuery=rtx%204070ti&pagingIndex=1&pagingSize=40&productSet=total&query=rtx%204070ti&sort=rel&timestamp=&viewType=list'

page = requests.get(SHOP_URL).text
data = BeautifulSoup(page, 'html.parser')

name = data.select_one('#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(1) > div > div > div.product_info_area__xxCTi > div.product_title__Mmw2K > a').text
price = data.select_one('#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(1) > div > div > div.product_info_area__xxCTi > div.product_price_area__eTg7I > strong > span > span.price_num__S2p_v > em').text


message1 = name
message2 = price + '원'

# 메세지 발송
requests.get(TELEGRAM_URL + message1 + '\n' + message2)






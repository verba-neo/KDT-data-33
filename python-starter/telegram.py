# telegram.py
import requests

# Bot 정보
TOKEN = '<my-bot-token>'
# 내 정보
MY_ID = '<my-chat-id>'

# 아래 URL 로 접속시 지금까지 bot이 받은 메시지들 확인 가능
'https://api.telegram.org/bot<token>/getUpdates'

URL = 'https://api.telegram.org/bot6826784028:AAGS-Sgbsc5eJQS6TR8Ygoh8Aax-bX8DucU/sendMessage?chat_id=765946187&text='
message = '여러분이 원하는것 무엇이든 담고'

# 메세지 발송
requests.get(URL + message)






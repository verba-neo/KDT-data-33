# lotto-api.py
import requests

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1096'

data = requests.get(URL).json()

print(data)
print(data['firstWinamnt'])


# dictionary => { Key : Value }
{
    "returnValue": "success",
    
    "totSellamnt": 105753078000,
    "firstAccumamnt": 25393911750,
    "firstPrzwnerCo": 10,
    "firstWinamnt": 2539391175,
    
    "drwNo": 1096,
    "drwNoDate": "2023-12-02",

    "drwtNo1": 1,
    "drwtNo2": 12,
    "drwtNo3": 16,
    "drwtNo4": 19,
    "drwtNo5": 23,
    "drwtNo6": 43,
    "bnusNo":  34,
}
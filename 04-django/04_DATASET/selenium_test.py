# selenium_test.py
# pip install selenium

import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


URL = 'https://map.kakao.com/'
driver = webdriver.Chrome()
driver.get(URL)

def wait_to_search(sec, selector):
    try:
        result = WebDriverWait(driver, sec).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        return result
    except:
        print(selector, '셀렉터로 검색 불가')
        driver.quit()


search_input = wait_to_search(5, '#search\.keyword\.query')
search_input.send_keys('고기집')
search_input.send_keys(Keys.ENTER)
time.sleep(1.5)
# 장소 탭 클릭
location_tab = wait_to_search(5, '#info\.main\.options > li.option1 > a')
location_tab.send_keys(Keys.ENTER)
time.sleep(1)

# csv 파일 쓰기
# f = open('kakao_places.csv', 'a', encoding='utf-8, newline='')
f = open('kakao_places.csv', 'w', newline='')
wr = csv.writer(f)
# csv 헤더 작성
wr.writerow(['name', 'category', 'score', 'score_count', 'review_count', 'address', 'detail_url'])

# page 고르기 (5페이지만 긁기)
for i in range(5):
    page = wait_to_search(3, f'#info\.search\.page\.no{i+1}')
    page.send_keys(Keys.ENTER)
    time.sleep(1)

    places = driver.find_elements(By.CSS_SELECTOR, '#info\.search\.place\.list > .PlaceItem')
    for place in places:
        html = place.get_attribute('innerHTML')
        soup = BeautifulSoup(html, 'html.parser')

        # HIDDEN 클래스가 있다 => 보여주는 중이다. 
        is_showing = bool(soup.select_one('div.rating.clickArea > span.txt_blind.HIDDEN'))
        if is_showing:
            name = soup.select_one('div.head_item.clickArea > strong > a.link_name').text
            category = soup.select_one('div.head_item.clickArea > span').text
            score_count = int(soup.select_one('div.rating.clickArea > span.score > a').text.rstrip('건').replace(',', ''))
            score = float(soup.select_one('div.rating.clickArea > span.score > em').text)
            review_count = int(soup.select_one('div.rating.clickArea > a > em').text.replace(',', ''))
            address = soup.select_one('div.info_item > div.addr > p:nth-child(1)').text
            detail_url = soup.select_one('div.info_item > div.contact.clickArea > a.moreview')['href']
            # 줄 추가
            wr.writerow([name, category, score, score_count, review_count, address, detail_url])
f.close()

# driver.get('https://google.com')
# time.sleep(3)
# store_link = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/a[2]')
# store_link.click()
# time.sleep(3)

# search_box = driver.find_element(By.CSS_SELECTOR, '#APjFqb')
# search_box.send_keys('점심메뉴')
# search_box.send_keys(Keys.RETURN)
# time.sleep(3)

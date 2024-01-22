# selenium_test
# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 크롬창을 띄우지 않는다.
# options = webdriver.ChromeOptions()
# options.add_argument('headless')

URL = 'https://map.kakao.com/'
driver = webdriver.Chrome()
driver.get(URL)







# import time
# driver.get('https://google.com')
# time.sleep(3)
# store_link = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/a[2]')
# store_link.click()
# time.sleep(3)


# search_box = driver.find_element(By.CSS_SELECTOR, '#APjFqb')
# search_box.send_keys('점심메뉴')
# search_box.send_keys(Keys.RETURN)
# time.sleep(3)

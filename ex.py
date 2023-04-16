from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# [2022.06.30] find_element_by_() 함수는 find_element(By., ) 과 같은 형태로 함수가 변경됨에 따른 추가 코드
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 드라이버 생성
# chromedriver 설치된 경로를 정확히 기재해야 함
chromedriver = 'C:/webdriver/chromedriver.exe' # 윈도우 
# chromedriver = '/usr/local/Cellar/chromedriver/chromedriver' # 맥

# [2022.06.30] find_element_by_() 함수는 find_element(By., ) 과 같은 형태로 함수가 변경됨에 따른 추가 코드
# driver = webdriver.Chrome(chromedriver)
driver = webdriver.Chrome(service=Service(chromedriver))

# 크롤링할 사이트 호출
driver.get("https://davelee-fun.github.io/blog/TEST/index.html")

# 여기에 고민하시면서 작성해보세요
elem = driver.find_element(By.ID,'username')
elem.send_keys('error@error.com')
sleep(1)

elem = driver.find_element(By.ID,'password')
elem.send_keys(1234)
sleep(1)

elem = driver.find_element(By.CSS_SELECTOR,'input[type="submit"]')
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.CSS_SELECTOR, "div.message")
print (elem.text)
sleep(2)

driver.quit()
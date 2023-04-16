from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# 크롬 드라이브의 경로
driver_path = 'C:/webdriver/chromedriver.exe'
# driver 객체 생성
driver = webdriver.Chrome(service=Service(driver_path))


# 목표 : python을 실행할 때 넣어둔 인자를 기준으로 찾아 엑셀로 정리
url = 'https://korean.visitkorea.or.kr/list/cs_list.do?areacode=All'
driver.get(url)
# driver를 통한 url 페이지 얻기 
# 정적페이지를 한번 받아오는 것이 아니라 계속 실행
# print(driver.title)
# popular_Button = driver.find_element(By.CSS_SELECTOR,'span.back_btn')
# link = driver.find_element(By.CSS_SELECTOR,'#contents > div.wrap_contView.clfix > div.box_leftType1 > ul > li:nth-child(1) > div.area_txt > div > a')
# onclick_value = link.get_attribute("onclick")
# params = onclick_value.split(",")
# params = [p.strip("'") for p in params]
# script = f"goDetail('{params[0]}', '{params[1]}', '{params[2]}')"  # 실행할 자바스크립트 코드 생성
# attrs = driver.execute_script(script)
# attrs.click() 
# sleep(5)
#  onclick_value = link.get_attribute("onclick")
# popular_Button.click()
# sleep(2)
# print(driver.current_url)
# sleep(5)

# 페이지에서 인기순인 것을 찾아 클릭하여 변환
# popular_Button = driver.find_element(By.ID,'3')
# popular_Button.click()

# # 페이지에서 연인코스인 것을 찾아 클릭하여 반환
# course_button = driver.find_element(By.ID,'146b6e3b-09e7-4312-aa50-1e748fdebdfe')
# course_button = course_button.find_element(By.TAG_NAME,'button')
# course_button.click()

# # 페이지소스 얻기
# # 1. 클릭할 곳 선택
# targets = driver.find_element(By.CSS_SELECTOR,'#contents > div.wrap_contView.clfix > div.box_leftType1 > ul > li:nth-child(1) > div.area_txt > div > a')
# print(targets)
# targets.click()
# print(driver.title)
# print(driver.current_url)
# sleep(3)
# driver.back
driver.quit()
# driver.switch_to.window(driver.window_handles[1])

# driver.switch_to.window(driver.window_handles[0])
# # 현재 URL 얻기 driver.current_url
# # driver.title로 제목 얻기
# sleep(3)
# driver.quit()
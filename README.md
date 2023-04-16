# 셀레니움을 이용한 동적 웹페이지 크롤링

## 순서
> VENV 라이브러리 가상환경설정

- 가상환경설정(venv)
- python -m venv venv
- source venv/Script/activate

> Git 환경설정
- git init
- github에서 원격저장소 만들기
- local에 github 원격저장소 연결 
- git remote add origin https://github.com/soomerss/Selenium_crawler.git
- git push origin master(처음)
- git push
- .gitignore -> venv 추가

> 필요 라이브러리 다운로드
* selenium, webdriver_manager
* pip install selenium, webdrver_manager

> 크롬 드라이브 다운로드 - 크롬 브라우저를 통해 작업할 것이며, 브라우저 Version에 반드시 맞추어 작업해야함
* https://chromedriver.chromium.org/downloads
* C:/webdriver/chromedriver - 임의로 해도 무방, 단,바탕화면에 두면 너무 길어짐

> 셀레니움을 이용한 웹 사이트 크롤링 및 엑셀 변환
* 코드를 통해 구현


> Issue
* [2023.04.16] a 태그의 href가 javaScript로 되어 있어 해당 페이지로 클릭하는 기능을 구현함에 어려움이 있음
# 셀레니움을 이용한 동적 웹페이지 크롤링

## 순서
> VENV와 Git 환경설정
- 가상환경설정(venv)
- python -m venv venv
- source venv/Script/activate
- .gitignore -> venv 추가

> 필요 라이브러리 다운로드
* selenium, webdriver_manager
* pip install selenium, webdrver_manager

> 크롬 드라이브 다운로드 - 크롬 브라우저를 통해 작업할 것이며, 브라우저 Version에 반드시 맞추어 작업해야함
* https://chromedriver.chromium.org/downloads
* C:/webdriver/chromedriver - 임의로 해도 무방, 단,바탕화면에 두면 너무 길어짐

> 웹 사이트 크롤링 및 엑셀 변환
* 코드를 통해 구현
"""
위정호
2021.06.16
네이버 코스콤 기사검색 RPA
"""
import time
import pywinmacro as pw

#마우스 장소 지정 1번은 링크창, 2번은 창닫기
location = (605, 78)
location1 = (1131, 18)

# 네이버에 접속하는 함수
def go_to_naver():
    # 주소창 클릭
    pw.click(location)
    time.sleep(2)
    # 네이버 주소 입력
    pw.type_in("https://naver.com")
    time.sleep(1)

# 엔터키 입력
    pw.key_press_once("enter")

#네이버 뉴스창에 접속하는 함수
go_to_naver()
time.sleep(3)

for i in range(26):
    pw.key_press_once("tab")
pw.key_press_once("enter")
time.sleep(1)

#뉴스 검색창으로 이동
for i in range(23):
    pw.key_press_once("tab")
time.sleep(2)

#뉴스 검색창에 코스콤 티커코드 입력
pw.type_in("코스콤")
pw.key_press_once("enter")

#뉴스창에서 첫번째 기사 클릭
for i in range(31):
    pw.key_press_once("tab")
time.sleep(2)
pw.key_press_once("enter")
time.sleep(10)
#기사 확인 후 창 닫기
pw.click(location1)
pw.l_click()

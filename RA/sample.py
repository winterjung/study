'''
뉴스 기사 크롤링
토픽 : 청계천
기간 : 청계천 복원사업 착수 이전(2003.07.01 이전)
출력물 형식 : json
출력물 포함 속성 : 제목, 내용, 일시

샘플한정 : 조선일보 1곳

조선일보 "청계천" 검색결과 최신순 정렬 링크
http://search.chosun.com/search/news.search?query=%EC%B2%AD%EA%B3%84%EC%B2%9C&pageno=502&orderby=docdatetime&c_scope=paging

2017.03.07기준 총 5692건
마지막 페이지 넘버 570(1993.01.18 기사)
시작 페이지 넘버 502(2003.07.01 기사)
'''
import json
import requests
from bs4 import BeautifulSoup


start_pg_num = 502
end_pg_num = 570
page_url = "http://search.chosun.com/search/news.search?query=%EC%B2%AD%EA%B3%84%EC%B2%9C&pageno={}&orderby=docdatetime&c_scope=paging".format(
    start_pg_num
)

r = requests.get(page_url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
news_result = soup.select("#result > div.result_box > section > dl")

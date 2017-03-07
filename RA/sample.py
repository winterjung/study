'''
뉴스 기사 크롤링
토픽 : 청계천
기간 : 청계천 복원사업 착수 이전(2003.07.01 이전)
출력물 형식 : json
출력물 포함 속성 : 제목, 내용, 일시
출력물 예시 : 
{
    "content_id_1": {
        "title": None,
        "date": None,
        "category": None,
        "text": None,
        "url": None,
    },
    "content_id_2": {

    },
}

샘플한정 : 조선일보 1곳

조선일보 "청계천" 검색결과 최신순 정렬 링크
http://search.chosun.com/search/news.search?query=%EC%B2%AD%EA%B3%84%EC%B2%9C&pageno=502&orderby=docdatetime&c_scope=paging

2017.03.07기준 총 5692건
마지막 페이지 넘버 570(1993.01.18 기사)
시작 페이지 넘버 502(2003.07.01 기사)
'''
import json
import requests
from collections import OrderedDict
from bs4 import BeautifulSoup

# 페이지 결과 가져오기
start_pg_num = 502
end_pg_num = 570
page_url = "http://search.chosun.com/search/news.search?query=%EC%B2%AD%EA%B3%84%EC%B2%9C&pageno={}&orderby=docdatetime&c_scope=paging".format(
    start_pg_num
)

# 뉴스 컨텐츠 영역만 파싱
r = requests.get(page_url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
news_result = soup.select("#result > div.result_box > section > dl")

# 결과물이 담길 dict
result = OrderedDict()

# 각각의 기사에서 구분번호, 제목, url, 분야 추출
for news in news_result:
    date = news.select("em")[0].get_text()
    title = news.select("dt > a")[0].get_text()
    category = news.select("a")[-1].get_text()
    url = news.select("dt > a")[0]["href"]
    content_id = url.split("contid=")[-1]
    result[content_id] = {
        "title": title,
        "date": date,
        "category": category,
        "text": None,
        "url": url,
    }

import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791185424194&orderClick=LAG&Kc=', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#select 를 이용해서, 제목정보를 불러오기
titles = soup.select('div[class=box_detail_point]>[class=title]')

#굳이 for을 쓰는 이유가 무엇일까?.. 반복문을 만들지 않아도 되지 않을까?
for title in titles:

#span class ="back" 내용인 '습관을 만드는 신상품 개발 모델' 을 제외하고 '훅[hooked]'만 갖고오려고 했는데 아무리 해도 안 된다.. ㅜ
#하위 태그인 span class:back 을 제외하기 위해 extract를 사용했는데 왜 '습관을 만드는 신상품 개발 모델' 만 결과로 나올까?.. ㅠ
    for title in soup.find_all('span',{'class': 'back'}):
        if title.span:
            _ = title.span.extract()

    print(title.text.strip())




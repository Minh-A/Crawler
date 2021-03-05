import urllib.request
from bs4 import BeautifulSoup as bs
import requests as req

word = input("아무거나 적으시오\n" )

url = 'https://search.naver.com/search.naver?query='+ word +'&nso=&where=blog&sm=tab_viw.all'
print(url)

html = req.get(url) # 불러오기
soup = bs(html.text, 'lxml')  # Beautifulsoup으로 분석

print("----")

# 30개씩 뽑아짐
for i in range(30):
    title = soup.select('a.api_txt_lines.total_tit')[i]
    print(title.text)













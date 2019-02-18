import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

# page_url = 'https://css-tricks.com/almanac/'

# page = urlopen(page_url)
# soup = BeautifulSoup(page, 'lxml')

# name_box = soup.select("div.selector-list a")

# for n in name_box:
#     a = str(n)
#     b = re.sub('<.*?>$','', re.sub('^<.*?>','', a))
#     print(b)

# page_url = 'https://news.google.com/'

# page = urlopen(page_url)
# soup = BeautifulSoup(page, 'lxml')

# name_box = soup.select("#yDmH0d > c-wiz > div > div.ajwQHc.BL5WZb.RELBvb.fV8ehb > div > aside > c-wiz > div.lBwEZb.BL5WZb.xP6mwf.zvAjsd > div.SXu5Cc.R7GTQ.keNKEd.j7vNaf > div > div.VjxR9 > div.LNrHIf > span")

# for n in name_box:
#     a = str(n)
#     b = re.sub('<.*?>$','', re.sub('^<.*?>','', a))
#     print(b)

page_url = 'https://www.bseindia.com/stock-share-price/city-union-bank-ltd/cub/532210/#!#equity'

page = urlopen(page_url)
soup = BeautifulSoup(page, 'html.parser')

# name_box = soup.select(".viewsensexvalue .ng-binding")
name_box = soup.select(".stockreach_title")
# name_box = soup.title()

# for n in name_box:
#     a = str(n)
#     b = re.sub('<.*?>$','', re.sub('^<.*?>','', a))
#     print(b)

print(soup)
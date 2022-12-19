from bs4 import BeautifulSoup
import requests
from datetime import datetime

resp = requests.get("http://www.srikanthtechnologies.com/rss.xml")
contents = resp.text
bs = BeautifulSoup(contents, 'lxml-xml')
items = bs.find_all("item")
for item in items:
    title = item.find("title").text
    link = item.find("link").text
    dates = item.find("pubDate").text

    startdate = datetime.strptime(dates, "%a, %d %b %Y %H:%M:%S")
    if startdate.year != 2022:
       continue
    else:
        print(dates)

    print(f"{title} {link} ")
    print("-------------------------------------------------------------------------------------------")
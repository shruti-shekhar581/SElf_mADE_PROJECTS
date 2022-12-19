from bs4 import BeautifulSoup
website="http://www.srikanthtechnologies.com"
import requests
resp=requests.get(website)
if resp.status_code!=200:
    print("sorry could not be found")
    exit()
contents=resp.text
bs=BeautifulSoup(contents,'html.parser')
links=bs.find_all("a")
for link in links:
    text=link.text
    url=link['href']
    print(link)
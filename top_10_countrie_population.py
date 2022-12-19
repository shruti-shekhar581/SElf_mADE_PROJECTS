import requests


resp=requests.get(f"https://restcountries.com/v2/all")
if resp.status_code!=200:
    print("sorry could not be found")
    exit()
countries=resp.json()
for country in sorted(countries,key=lambda  c:c['population'],reverse=True)[:10] :
    name=country["name"]
    population=country['population']
    area=country['area']
    print(f"{ name:50} {population:10} { area:10}")
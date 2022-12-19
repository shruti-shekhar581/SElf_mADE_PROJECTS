import requests


resp=requests.get(f"https://restcountries.com/v2/all")
if resp.status_code!=200:
    print("sorry could not be found")
    exit()
details=resp.json()
Datetime=details['datetime']
print(f"{ Datetime : 5}")

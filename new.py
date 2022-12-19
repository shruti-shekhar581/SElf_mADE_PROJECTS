import requests
code = input("Enter country code :")
resp = requests.get (f"https://restcountries.com/v3.1/alpha/{code}")
if resp.status_code == 404:
    print("Sorry! Country code not found!")
elif resp.status_code != 200:
    print("Sorry! Could not get country details!")
else: # Take first elements in the list of dictionaries
     details = resp.json()[0]
     print("Country Information");
     print("Name : " + details["name"]["common"])
     print("Capital : " + details["capital"][0])
     print("Population : " + str(details["population"]))
     print("Sharing borders with :")
     for c in details["borders"]:
        print(c)
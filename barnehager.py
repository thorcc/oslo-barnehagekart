import json
import requests
import time

with open('barnehager-oslo.json', encoding='utf-8') as file:
    data = json.load(file)

kindergartens = [{'name': k['name'], 'address': k['card_data']['address']} for k in data['hits']]

i = 0
tot = len(kindergartens)
for k in kindergartens:
    try:
        q = k["address"].replace(" ", "+").replace(",","")
        url = 'https://nominatim.openstreetmap.org/search?format=json&q=' + q
        res = requests.get(url, headers={"User-Agent": "barnehage-geocoder/1.0"})
        j = res.json()
        k['lat'] = j[0]["lat"]
        k['lon'] = j[0]["lon"]
        with open('barnehager.json', 'w', encoding='utf-8') as file:
            json.dump(kindergartens, file, ensure_ascii=False, indent=2)
    except:
        print(f"Err: skipping {k['name']}")
    i+=1
    print(f"{i}/{tot}")
    time.sleep(1)


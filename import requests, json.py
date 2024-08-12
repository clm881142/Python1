import requests, json

url = 'https://api.hkma.gov.hk/public/recruitment?lang=en&offset=0'
resp = requests.get(url)
web_data = resp.content
hkma = json.loads(web_data)
print(hkma)

data_keyword = "data" and "it" and "manager"
filtered_records = []

for record in hkma["result"]["records"]:
    if data_keyword in record["title"].lower():
        filtered_records.append(record)
index = 1

for i in filtered_records:

    print( "job", index,"-", record["title"],"-", record["link"])
    index = index + 1
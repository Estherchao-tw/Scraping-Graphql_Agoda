import requests
import json

f = open('agoda_query.json')
data = json.load(f)

url = "https://www.agoda.com/graphql/search"
headers = {
    "Content-Type": "application/json",
    "Ag-Language-Locale": "zh-tw",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
response = requests.request("POST",url,headers=headers,json=data)

print(response.json())


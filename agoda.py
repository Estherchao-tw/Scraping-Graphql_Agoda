import requests
from bs4 import BeautifulSoup

url = "https://www.agoda.com/graphql/search"

payload = {
    "operationName": "citySearch",
    "variables": {
        "CitySearchRequest": {},
        "ContentSummaryRequest": {},
        "PricingSummaryRequest": {},
        "PriceStreamMetaLabRequest": {}
    },
    "query": "query citySearch($CitySearchRequest: CitySearchRequest!, $ContentSummaryRequest: ContentSummaryRequest!, ......"
}

headers = {
    "Content-Type": "application/json",
    "Ag-Language-Locale": "zh-tw",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

response = requests.request("POST",url,headers=headers,data=payload)
print(response.text)
print(response.status_code)

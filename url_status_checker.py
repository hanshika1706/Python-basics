#url_status_checker.py

import requests

url = input("Enter URL: ")
res = requests.get(url)

print("Status Code:", res.status_code)

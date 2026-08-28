import requests

url = "https://tradead.tixplus.jp/giants"

response = requests.get(url, timeout=30)

print("ステータス:", response.status_code)
print("取得文字数:", len(response.text))
print(response.text[:1000])

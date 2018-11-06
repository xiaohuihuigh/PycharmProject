import requests
proxy = {
    # "socks5": "http://127.0.0.1:1080"
   "https": "https://127.0.0.1:1080",
   "http": "https://127.0.0.1:1080"
}
data = requests.get("https://www.google.com", proxies=proxy)
# data = requests.get("https://www.baidu.com")
print(data.status_code)
print(data.text)
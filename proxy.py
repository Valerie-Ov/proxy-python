import requests


proxies = {
    'http': 'http://127.0.0.1:8899',
    'https': 'http://127.0.0.1:8899',
}
response = requests.get('http://google.com', proxies=proxies)
print(response.text)
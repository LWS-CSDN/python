import requests

proxies={
    "http":"http://77.77.1:80"
}
resp=requests.get('http://www.baidu.com',proxies=proxies)
resp.encoding='utf-8'
print(resp.text)
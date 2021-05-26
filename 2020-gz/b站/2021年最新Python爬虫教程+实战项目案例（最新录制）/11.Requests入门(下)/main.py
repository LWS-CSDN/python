import requests
url="http://www.sogou.com/web?query=周杰伦"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}
#处理了一个小小的反爬
resp=requests.get(url,headers=headers)
print(resp.text)
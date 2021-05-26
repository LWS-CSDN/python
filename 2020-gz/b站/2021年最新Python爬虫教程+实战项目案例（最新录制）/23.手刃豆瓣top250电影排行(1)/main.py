import re
import requests

url="http://movie.douban.com/top250"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}
resp=requests.get(url,headers=headers)
page_content=resp.text

#解析数据
obj=re.compile(r'<li><span class="title">(?P<name>.*?)</span>',re.S)

#开始匹配
print(page_content)
result=obj.finditer(page_content)
print(result)
for it in result:
    print(it.group("name"))
import requests
from  lxml import etree
url="https://beijing.zbj.com/search/f/?type=new&kw=sass"

resp=requests.get(url)

html=etree.HTML(resp.text)
divs=html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div/div[1]")
for div in divs:
    price=div.xpath("./div/div/a/div[2]/div[1]/span[1]/text()")
    print(price)
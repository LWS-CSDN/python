# -*- coding: utf-8 -*-
import scrapy


class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.qiushibaike.com/text/']

    def parse(self, response):
        #解析:作者的名称+段子内容
        div_list=response.xpath('//div[@id="content"]/div[1]/div[2]/div')
        print("div_list:",div_list)
        for div in div_list:
            author=div.xpath('./div[1]/a[2]/text()')[0]
            content=div.xpath('./a[1]/div/span[1]//text()')
            print("author:",author,"content:",content)
            break

'''
1.创建一个工程:scrapy startproject firstBlood(项目名字)
2.cd firstBlood(项目名字)
3.在spiders子目录中创建一个爬虫文件
scrapy genspider spiderName(爬虫的名字) www.xxx.com
4.把遵从roobt协议改为False,一般都不遵从,要不没法爬取
在settings.py文件里
5.执行工程:
-scrapy crawl spiderName(爬虫的名字)
-scrapy crawl spiderName -iubaiqi-nlog(日志太多不想看,但是报错看不到了)

在settings.py的文件里设置
#显示指定类型的日志信息
LOG_LEVEL='ERROR'
再用scrapy crawl spiderName
'''

import builtwith
import ssl
import whois
'''
识别网站所用的技术
'''
a=builtwith.parse('')
print(a)

ssl._create_default_https_context = ssl._create_unverified_context
a=builtwith.parse('')
print(a)


whois.whois('baidu.com')

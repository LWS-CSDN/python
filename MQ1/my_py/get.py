from urllib import request
import tornado
import tornado.httpclient 
import threading


def get(url):
    '''
    url:必填项
    '''
    http_client = tornado.httpclient.HTTPClient()
    try:
        response = http_client.fetch(url,verify=False)
        print(response.body)
    except tornado.httpclient.HTTPError as e:
        # HTTPError is raised for non-200 responses; the response
        # can be found in e.response.
        print("Error: " + str(e))
    except Exception as e:
        # Other errors are possible, such as IOError.
        print("Error: " + str(e))
    http_client.close()
def post(url,data):
    pass
get("https://www.baidu.com")

# post('',data)




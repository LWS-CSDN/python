# coding=utf-8
import tornado.web
import tornado.ioloop
import time
import random

class UploadHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.set_header("Access-Control-Allow-Origin", "*") # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        cpu=random.randint(0,100)
        #self.write({'result':'ok', 'cpu': cpu})
        data='''{
        "status": "success",
        "totals": 3,
        "data": [
            {
                "id": 9,
                "author": "33",
                "praiseNumber": "0",
                "status": 1,
                "readNumber": 146,
                "pic": "/upload/blog/pic/2936_listManager.png",
                "title": "listManager使用详解",
                "subtitle": "",
                "type": 3,
                "info": "适用于管理平台的数据展示列表，通过该插件可以更简约的实现一些前端交互及与列表相关的功能实现。",
                "createDate": 1460364938000,
                "lastDate": 1460365932827,
                "commentSum": 1,
                "username": "写个程序换个饼",
                "photo": "/upload/user/photo/8495_1.jpg",
                "l_content":"荣昌中学1"
            },
            {
                "id": 8,
                "author": "33",
                "praiseNumber": "0",
                "status": 1,
                "readNumber": 311,
                "pic": "/upload/blog/pic/9870_1594621862038.png",
                "title": "margin-top 外边距合并",
                "subtitle": "css",
                "type": 1,
                "info": "margin-top 外边距合并的边距合并的触发条件及解决方式",
                "createDate": 1457330074000,
                "lastDate": 1594621873579,
                "commentSum": 3,
                "username": "写个程序换个饼",
                "photo": "/upload/user/photo/8495_1.jpg",
                "l_content":"荣昌中学2"
            },
            {
                "id": 7,
                "author": "33",
                "praiseNumber": "0",
                "status": 1,
                "readNumber": 714,
                "pic": "/upload/blog/pic/5120_1594621430986.png",
                "title": "JSON.stringify()执行出错",
                "subtitle": "js",
                "type": 3,
                "info": "执行JSON.stringify() 抛出的错误信息：Uncaught TypeError: Converting circular structure to JSON",
                "createDate": 1456402852000,
                "lastDate": 1594621479023,
                "commentSum": 5,
                "username": "写个程序换个饼",
                "photo": "/upload/user/photo/8495_1.jpg",
                "l_content":"荣昌中学3"
            },
            {
                "id": 6,
                "author": "33",
                "praiseNumber": "0",
                "status": 1,
                "readNumber": 434,
                "pic": "/upload/blog/pic/3327_1594621385587.jpg",
                "title": "前端国际化",
                "subtitle": "国际化",
                "type": 3,
                "info": "从10年接触编程就开始接触国际化这个概念，这些年项目中做到国际化的项目并不是很多，零星项目中做的都是无非也都是螺丝钉的工作。15年末，部门项目需要推国际化，前端这块由我来主导。虽然难度不高，但还是拿出来分享下。",
                "createDate": 1456314006000,
                "lastDate": 1594621388566,
                "commentSum": 7,
                "username": "写个程序换个饼",
                "photo": "/upload/user/photo/8495_1.jpg",
                "l_content":"荣昌中学4"
            },
            {
                "id": 4,
                "author": "33",
                "praiseNumber": "0",
                "status": 1,
                "readNumber": 164,
                "pic": "/upload/blog/pic/7373_1.jpg",
                "title": "UEdit 使用总结",
                "subtitle": "",
                "type": 3,
                "info": "最近项目中频繁使用到 uedit，在使用中遇到一些磕磕绊绊的事。",
                "createDate": 1404187620000,
                "lastDate": 1456320676925,
                "commentSum": 0,
                "username": "写个程序换个饼",
                "photo": "/upload/user/photo/8495_1.jpg",
                "l_content":"荣昌中学5"
            },
            {
                "id": 5,
                "author": "33",
                "praiseNumber": "0",
                "status": 1,
                "readNumber": 210,
                "pic": "/upload/blog/pic/9819_2.jpg",
                "title": "自定义表单、流程、菜单开发总结",
                "subtitle": "",
                "type": 3,
                "info": "最近在做自定义表单、自定义流程、自定义菜单，由于某些原因，现在这个项目正处于停滞状态。但核心功能已实现，做点总结拿出来分享。",
                "createDate": 1403323560000,
                "lastDate": 1456320687638,
                "commentSum": 5,
                "username": "写个程序换个饼",
                "photo": "/upload/user/photo/8495_1.jpg",
                "l_content":"荣昌中学6"
            }
        ]}'''
        print("data",data)
        print("type",type(data))
        import json
        
        #self.write(data)
        self.finish(data)
        #self.write({'result':'ok', 'cpu': cpu})
    def post(self,*args,**kwargs):
        #获取请求参数
        print("self:",self)
        print("self.request:",self.request)
        print("self.request.files:",self.request.files)
        print("self.request.files[\"img1\"]:",self.request.files["img1"])
        
        img1=self.request.files['img1']
        for img in img1:
            body=img.get('body','')
            content_type=img.get('content_type','')
            filename=img.get('filename','')
           
        '''
        这里需要手动创建files文件,后期修复
        '''
        #将图片存放至files目录中
        import os
        dir=os.path.join(os.getcwd(),'files',filename)

        with open(dir,'wb') as fw:
            fw.write(body)

        #将图片显示到浏览器页面中
        #设置响应头信息
        self.set_header('Content-Type',content_type)
        self.write(body)

        

app=tornado.web.Application([
    (r'/',UploadHandler)
])

app.listen(9998)

tornado.ioloop.IOLoop.instance().start()















# def parse_icon(filePath, file):

#     print(file)
#     print(FOLDER_MAIN)
#     zong = FOLDER_MAIN.replace('\\', '/')
#     print(zong+"/img/icon_"+file+".bmp")
#     large, small = win32gui.ExtractIconEx(filePath, 0)
#     win32gui.DestroyIcon(small[0])
#     hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
#     hbmp = win32ui.CreateBitmap()
#     hbmp.CreateCompatibleBitmap(hdc, 32, 32)
#     hdc = hdc.CreateCompatibleDC()
#     hdc.SelectObject(hbmp)
#     hdc.DrawIcon((0, 0), large[0])
#     hbmp.SaveBitmapFile(hdc, zong+"/img/icon_"+file+".bmp")


# def parse_iconall():
#     path = FOLDER_MAIN+"/upload/"
#     folds = os.listdir(path)
#     for subfold in folds:
#         fpath = path + subfold
#         if os.path.isdir(fpath):
#             result = os.listdir(fpath)
#             print("result", result)
#             if result != '':
#                 for file in result:
#                     if file[-4:] == '.exe':
#                         parse_icon(fpath+"/"+file, file)
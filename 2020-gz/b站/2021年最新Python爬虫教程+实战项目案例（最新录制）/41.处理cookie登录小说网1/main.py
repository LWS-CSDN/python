import requests

#会话
# session=requests.session()
# data={
#     "loginName":"***********",
#     "password":"*********"
# }
# #1.登录
# url="https://passport.17k.com/ck/user/login"
# resp=session.post(url,data=data)
# print(resp.text)
# print(resp.cookies)
#
# #2.拿书架上的数据
# #刚才的那个session中是有cookie的
# resp=session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
# print(resp.json())




#路子太野
# resp=requests.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919',headers={
#     "Cookie": "**************"
# })
# print(resp.text)
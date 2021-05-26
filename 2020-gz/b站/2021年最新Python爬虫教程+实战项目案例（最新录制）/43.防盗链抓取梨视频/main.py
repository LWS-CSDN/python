#1.拿到contId
#2.拿到videoStatus返回的json ->srcURL
#3.srcURL里面的内容进行修整
#4.下载视频
import requests
url="https://www.pearvideo.com/video_1724948"
contId=url.split("_")[1]

videoStatusUrl=f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.4358743658482369"
headers={
    "Referer":"https://www.pearvideo.com/video_1724948"
}
resp=requests.get(videoStatusUrl,headers=headers)
dic=resp.json()
print(dic)
srcUrl=dic['videoInfo']['videos']['srcUrl']
systemTime=dic['systemTime']
srcUrl=srcUrl.replace(systemTime,f"cont-{contId}")
print(srcUrl)

#下载视频
with open("a.mp4",mode='wb') as f:
    f.write(requests.get(srcUrl).content)
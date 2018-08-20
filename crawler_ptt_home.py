#抓取網頁資料
import urllib.request as request
import ssl #憑證的套件
import bs4

def getData(url):
    context = ssl._create_unverified_context()
    req= request.Request(url,headers={
    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
})
    with request.urlopen(req,context=context) as response:
        data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data,"html.parser")
    titles = root.find_all("div","title")
    titleList=[]
    for title in titles:
        if title.a != None:  #有時候a標籤不存在
            titleList.append(title.a.string)
    # print(titleList)

    #按下一頁
    nextLink = root.find("a", string="‹ 上頁")
    next = nextLink["href"]
    return {
        "titles":titleList,
        "next":next,
    }

#建立分析資料的函示
cities={
    "台北":0,
    "新北":0,
    "桃園":0,
    "台中":0,
    "台南":0,
    "高雄":0,
}
def analyzeData(titles):
    for title in titles:
        for name in cities:
            if name in title:
                cities[name]+=1

#使用getData函式
host = "https://www.ptt.cc"
url = host + "/bbs/home-sale/index.html"
for i in range(3):
    data=getData(url)
    analyzeData(data["titles"])
    url = host+data["next"] #抓取下一頁的資料

#用圓餅圖畫出來
# print(cities)
import plotly.plotly as py
import plotly.graph_objs as go

labels = []
values = []
for name in cities:
    labels.append(name)
    values.append(cities[name])
print(cities)
print(labels)
print(values)
data = go.Pie(
    labels=labels,
    values=values
)
py.plot([data],filename="ptt_home_analyze")

#抓取網頁資料
import urllib.request as request
import ssl #憑證的套件
context = ssl._create_unverified_context()
url="https://www.ptt.cc/bbs/Gossiping/index.html"
req= request.Request(url,headers={
    "cookie" : "over18=1",
    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
})
with request.urlopen(req,context=context) as response:
    data = response.read().decode("utf-8")

#使用BeautifulSoup擷取目標文字
import bs4
root = bs4.BeautifulSoup(data,"html.parser")
titles = root.find_all("div","title")#找出< div class="title">......<div>
for title in titles:
    print(title.a.string)

# titles=root.find_all("h3")#會以列表的方式列印出來
# for title in titles:
#     print(title.string)
#抓取網頁資料
import urllib.request as request
import ssl #憑證的套件
context = ssl._create_unverified_context()
url="https://www.dcard.tw/f/food"
req= request.Request(url,headers={
    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
})
with request.urlopen(req,context=context) as response:
    data = response.read().decode("utf-8")

#使用BeautifulSoup擷取目標文字
import bs4
root = bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("h3")#會以列表的方式列印出來
for title in titles:
    print(title.string)
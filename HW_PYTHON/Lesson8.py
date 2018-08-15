#網頁爬蟲技術
# import requests
# requests.get()
# requests.post()
# requests.put()
# requests.delete()
# requests.patch()

# #URL傳參值/獲取請求的URL
# url1 = "https://www.urbanoutfitters.com/"
# #Requests 允许你使用 params 关键字参数，以一个字符串字典来提供这些参数。
# utm = {"utm_source":"google","utm_medium":"cpc"}
# r = requests.get(url1,params=utm)
# print(r.url)

#抓取yahoo!電影的某部電影, 例如:https://movies.yahoo.com.tw/movieinfo_main.html/id=5644
# 需要抓取的資訊如下:
# 電影名稱 (中英)
# 上映日期
# 類 型
# 片 長
# 導 演
# 演 員
# 發行公司
# 官方網站
# 劇情介紹
import urllib.request as request
import bs4 #使用BeautifulSoup擷取目標文字
import ssl
context = ssl._create_unverified_context()
url = "https://movies.yahoo.com.tw/movieinfo_main.html/id=5644"
headers = {
    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

with request.urlopen(url,context=context) as response:
    data = response.read().decode("utf-8")

# root = bs4.BeautifulSoup(data,"html.parser")

#官方網站資料抓取
# web = root.find_all(text="官方網站"))
# print(web.string)

#  劇情介紹
# title = root.find("div","gray_infobox_inner")
# print("劇情介紹：",title.text)
# #將電影種類資料抓取下來
# test = root.find_all("div","level_name")
# for catagory in test[:2]:
#     print("類型：",catagory.text,end="")


with open("5644.txt","w",encoding ="utf-8") as file :
    root = bs4.BeautifulSoup(data,"html.parser")
    #找出電影名稱
    movie_zh = root.find_all("h1")
    movie_eg = root.find_all("h3")

    file.write("電影名稱(中文):"+movie_zh[0].string+"\n")
    file.write("電影名稱(英文):"+movie_eg[0].string+"\n")
    #  劇情介紹
    title = root.find("div","gray_infobox_inner")
    file.write("劇情介紹："+title.text+"\n")
    # 將電影種類資料抓取下來
    test = root.find_all("div","level_name")
    for catagory in test[:2]:
        file.write("類型："+catagory.text+"\n")



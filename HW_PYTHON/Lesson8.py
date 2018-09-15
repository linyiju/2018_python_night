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
import re

context = ssl._create_unverified_context()
url = "https://movies.yahoo.com.tw/movieinfo_main.html/id=5644"
headers = {
    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

# with request.urlopen(url,context=context) as response:
#     data = response.read().decode("utf-8")

# all_page = bs4.BeautifulSoup(data,"html.parser")
# page = all_page.find("div","movie_intro_info_r")

# #電影的名稱(中文、英文)
# movie_zh = page.find("h1")
# print("電影名稱(中文):",movie_zh.text)

# movie_eg = page.find("h3")
# print("電影名稱(中文):",movie_eg.text)

# #電影種類資料
# catagorys = page.find_all("div","level_name")
# for catagory in catagorys :
#     print("電影種類:",catagory.text.strip())

# #上映日期、片長、發行公司、IMDb分數
# datas = page.find_all("span")
# for data in datas[:4]:
#     print(data.text)

# # 導演資料、電影演員資料2
# movie_intro_list = page.find_all("div","movie_intro_list")
# print("導演：",movie_intro_list[0].text.strip()) #導演資料
# new_actors = str(movie_intro_list[1].text.strip()).replace("\n","")
# print("演員：",new_actors) #演員資料


# actors = root.find_all("div","actor_inner")
# # print(actors)
# for actor in actors:
#     print("主要演員：",end="")
#     for child in actor.h2:
#         if child.string!=None:
#             print(child.string.strip().replace("\n",""),end="")
#             # if  child.string!=None:
#                 # print(child.string.strip().replace("\n",""),end="")
#     print("\n")

   

# #官方網站資料抓取
# web = page.find("a",{"href":"https://www.facebook.com/foxmovies.tw"})
# print("官方網站:"+web["href"]+"\n")

# #  劇情介紹
# title = all_page.find("div","gray_infobox_inner")
# print("劇情介紹：",title.text)


##  將爬到的資料寫入txt檔裡面

def movie_info(url):
    context = ssl._create_unverified_context()
    headers = {
    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }  
    with request.urlopen(url,context=context) as response:
        data = response.read().decode("utf-8") 
        all_page = bs4.BeautifulSoup(data,"html.parser")
        page = all_page.find("div","movie_intro_info_r")
        movie_zh = page.find("h1")
        movie_zh = movie_zh.text
    with open(movie_zh,"w",encoding ="utf-8") as file :

        #電影的名稱(中文、英文)
        movie_zh = page.find("h1")
        file.write("電影名稱(中文):"+movie_zh.text+"\n")

        movie_eg = page.find("h3")
        file.write("電影名稱(英文):"+movie_eg.text+"\n")

        #電影種類資料
        catagorys = page.find_all("div","level_name")
        for catagory in catagorys :
            file.write("電影種類:"+catagory.text.strip()+"\n")

        #上映日期、片長、發行公司、IMDb分數
        datas = page.find_all("span")
        for data in datas[:4]:
            file.write(data.text+"\n")

        # 導演資料、電影演員資料2
        movie_intro_list = page.find_all("div","movie_intro_list")
        file.write("導演："+movie_intro_list[0].text.strip()+"\n") #導演資料
        new_actors = str(movie_intro_list[1].text.strip()).replace("\n","")
        file.write("演員："+new_actors+"\n") #演員資料

        #官方網站資料抓取
        web = page.find("a",{"href":"https://www.facebook.com/foxmovies.tw"})
        file.write("官方網站:"+web["href"]+"\n")

        #  劇情介紹
        title = all_page.find("div","gray_infobox_inner")
        file.write("劇情介紹："+title.text+"\n")


movie_info("https://movies.yahoo.com.tw/movieinfo_main/%E9%A9%9A%E5%A5%874%E8%B6%85%E4%BA%BA-the-fantastic-four-5644")
import urllib.request as request
import bs4 #使用BeautifulSoup擷取目標文字
import ssl
import re
def movie_info(url):
    context = ssl._create_unverified_context()
    headers = {
    "user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }  
    with request.urlopen(url,context=context) as response:
        data = response.read().decode("utf-8") 
    
    root = bs4.BeautifulSoup(data,"html.parser")
    #找出電影的名稱
    movie= root.find_all("h1")
    movie_name = movie[0].string
    #將抓出的資料寫進txt檔，並以電影名稱命名
    with open(movie_name,"w",encoding ="utf-8") as file :
    #找出電影名稱
        movie_zh = root.find_all("h1")
        movie_eg = root.find_all("h3")
        file.write("電影名稱(中文):"+movie_zh[0].string+"\n")
        file.write("電影名稱(英文):"+movie_eg[0].string+"\n")
    
    #  劇情介紹
        title = root.find("div","gray_infobox_inner")
        file.write("劇情介紹："+"\n"+title.text.strip()+"\n")
    
    # 將電影種類資料抓取下來
        test = root.find_all("div","level_name")
        for catagory in test[:2]:
            file.write("類型："+catagory.text.strip()+"\n")
    
    # 電影演員資料2
        actors = root("div","actor_inner")
    # print(actors)
        for actor in actors:
            # file.write("主要演員："+end="")
            file.write("主要演員：")
            # file.write()
            for child in actor.h2:
                if child.string!=None:
                    file.write(child.string.strip().replace("\n",""))
                # if  child.string!=None:
                    # print(child.string.strip().replace("\n",""),end="")
            file.write("\n")
    
        # #官方網站
        # web = root.find("a",{"href":"https://www.facebook.com/foxmovies.tw"})
        # file.write("官方網站:"+web["href"]+"\n")

        #導演資料
        dictor = root.find_all("div","movie_intro_list")
        file.write("導演："+dictor[0].text.strip()+"\n")

movie_info("https://movies.yahoo.com.tw/movieinfo_main/%E6%AE%BA%E6%88%AE%E5%85%83%E5%B9%B4-the-first-purge-8062")
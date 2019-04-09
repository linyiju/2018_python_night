# 《20180723_HW4》
# 1.使用台北市公開資料的「臺北市臺北旅遊網-景點資料(中文)」
# 2.使用者可以用捷運站名稱搜尋景點
# 3.將對應到的景點資料，儲存在檔案中

#從網址讀取資料


import urllib.request as request
import json

with request.urlopen("http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=36847f3f-deff-4183-a5bb-800737591de5") as respone:
    data=json.load(respone)
    # print(data)


with open("attraction.txt","w",encoding ="utf-8") as file :
    keyword = input("請輸入捷運站名：")
    list = data["result"]["results"]
    file.write("站名："+keyword)
    for attractions in list:
        if keyword == attractions["MRT"]:
            # file.wrtie("站名：",keyword)
            print(attractions["stitle"])
            file.write(attractions["stitle"]+"\n")
##集合的運算
# s1 = {3,2,5}
# print(3 in s1)
# print(10  not in s1)
# print(4 not in s1)
# print(4 in s1)

# s1 = {2,3,4}
# s2 = {1,3}
# s3 = s1 & s2 #取s1和s2的交集
# s4 = s1 | s2 #取s1和s2的聯集
# s5 = s1 - s2 #差集：取兩個集合裡，不重疊的資料
# s6 = s1 ^ s2
# print(s3)
# print(s4)
# print(s5)
# print(s6)

# s= set("Hello") #set(字串) 沒有順序
# print(s)

# # 字典 Dictionary
# dic ={"apple":"蘋果", "bug":"蟲"}
# dic["apple"] = "小太陽" #更換key的value
# print(dic["apple"])
# print("apple" in dic) #in判斷的對象是字典裡的key

# dic2 = {"orange":"橘子","computer":"電腦","cup":"杯子"}
# del dic2["computer"] #刪除字典裡的鍵值對(key-value)
# print(dic2)


dic={x:x*2 for x in [3,4,5]} #從列表的資料去產生字典
print(dic)
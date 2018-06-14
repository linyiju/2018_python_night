# # #有序可變動列表 List
# # grade = [20, 60, 30, 100, 87]
# # #把75放入列表中第一個位子
# # grade[0] = 75
# # #把列表中連續刪除編號1到編號3(不包含) 
# # grade[1:3] = []
# # print(grade)

# # #簡單加入新數字
# # grade = grade + [40, 33, 90]
# # print(grade)
# # length =len(grade)
# # print(length)
# # # print(grade[3])
# # #取得列表中前3個資料
# # # print(grade[:3])


# #####NEW#####
# data = [[3,4,5],[6,7,8]]
# print(data[1][2])

# data[0][1:] = [6,9,12]
# print(data)

##Tuple
data = (3,4,5)
#data[0] = [3] #error: Tuple 的資料不可以變動
print(data)
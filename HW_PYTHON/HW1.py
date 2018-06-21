
####____動動腦____###
# #num = '1000'   #str字串型態
# #若需要除以2運算後得到數字500的話怎麼辦？

num = '1000'
x= int(num)
print(x/2)

# #nums=[1,1,1,2,2,3,4,5]
# #若需要將重複的元素去除的話怎麼辦
nums = [1,1,1,2,2,3,4,5]
l = list(set(nums))
print(l)

# # nums = (10,5,7,1,6,2)
# #tuple並不提供排序的⽅法，若要排序(由⼩到⼤)該怎辦？

nums = (10,5,7,1,6,2)
nums = list(nums)
nums.sort()
print(nums)

###____Homework1____###
# Q1. 使⽤set型別完成下列問題: 本班期末考試
# 數學及格的有: Tom, John, Mary, Jimmy, Sunny, Amy
# 英⽂及格的有: John, Mary , Tony , Bob , Pony, Tom , Alice
# 分別印出數學及格但英⽂不及格的名單，數學不及格但英⽂及格的名單，兩科都及格的名單
# 最後印出全班總共有幾個同學
math = {"Tom", "John", "Mary", "Jimmy", "Sunny", "Amy"}
eng = {"John", "Mary" , "Tony" , "Bob" , "Pony", "Tom" , "Alice"}
math_good = math - eng 
eng_good = eng - math
good = (math & eng)
all_students = len(math | eng)
print("數學及格但英⽂不及格的名單:",math_good)
print("數學不及格但英⽂及格的名單:",eng_good)
print("兩科都及格的名單:",good)
print("全班總共 ",all_students," 位學生")

# Q2. 使⽤dict，list 型別完成下列問題:
# Tom 作業成績為 80, 100, 90, 95，John 作業成績為 100,93,75,80
# 請以dict 型別存放兩個同學的資料 key:名字，value:分數列表(list)
# 請分別算出兩位同學的平均分數並且印出
dic ={"Tom":[80, 100, 90, 95],"John":[100,93,75,80]}
Tom_mean = sum(dic["Tom"])/len(dic["Tom"])
John_mean = sum(dic["John"])/len(dic["John"]) 
print("Tom平均分數：",Tom_mean)
print("John平均分數：",John_mean)

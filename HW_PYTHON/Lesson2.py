###if, elif, else 範例 ###
# 計算BMI並輸出分級值
BMI = 體重 (kg) / 身高 (m^2)
print("*計算BMI*")
kg = int(input("請輸入你的體重："))
m = int(input("請輸入你的身高："))

bmi = round(kg / (m/100)**2 ,2)
if bmi < 18.5 :
    print("你的 BMI是：",bmi,",體重過輕")
elif 18.5<= bmi <24:
    print("你的 BMI是：",bmi,",正常範圍")
elif 24<= bmi <27:
    print("你的 BMI是：",bmi,",輕度肥胖")
elif 27<= bmi <30:
    print("你的 BMI是：",bmi,",中度肥胖")
else:
    print("你的 BMI是：",bmi,",重度肥胖")


#for 迴圈範例
#輸入一個數字n，計算1+2+3+....+n的總和為多少？
n = int(input("請輸入數字:"))
sum = 0
for i in range(1,n+1) :
    sum +=i
    #print(sum,i)
print(sum)


###____Homework2____###
#分別用for，while迴圈各寫⼀個nxn的乘法表 程式可以讀取使用者輸入的值 n, n>1 
n =int(input("請輸入一個數字："))
i = 1
j = 1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i , "*" , j ,"=", i*j)
    
while i <= n :
    j=1
    while j <=n:
        print(i , "*" , j ,"=", i*j)
        j+=1
    i+=1
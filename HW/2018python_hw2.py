# 作業一
# n1 = int(input("Enter a number:"))
# n2 = int(input("Enter a number:"))
# op = input("運算符號(+，-，*，/)：")
# op為字串
# 幫使用者運算
n1 = int(input("請輸入n1的數值:"))
n2 = int(input("請輸入n2的數值:"))
op = input("請輸入 +, -, *, / :")
if op=="+":
    print("得到的數值為：",n1+n2)
elif op =="-":
    print("得到的數值為：",n1-n2)
elif op =="*":
    print("得到的數值為：",n1*n2)
elif op =="/":
    print("得到的數值為：",n1/n2)
else :
    print("輸入錯誤")


# 作業二
# n = int(input("輸入一個正整數"))
# 算整數平方根 9=>3, 25=>5, 8=>沒有
# 1,2,3,4,5
n =int (input("請輸入一正整數:"))
for i in range(n):
    if i * i == n :
        print("平方根為：",i)
        break
else:
    print(n,"沒有正整數平方根喔")

# 作業三
# 列印9*9乘法表
for i in range(1,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j)
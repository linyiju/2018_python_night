# #判斷式
#if 判斷式
#if 布林值：
#   如果布林值是True 執行這個程式區塊
if True :
    print("Hello")
x = int(input("請輸入一個數值:"))
if x>20:
    print("大於20")
elif x>10:
    print("小於10")
else:
    print("太小囉！")

#數字的四則運算
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

money = int(input("多少錢？"))
if money <= 0:
    if money.isnumeric():
        print("請輸入大於０的數字")
    else:
        print("w")   
elif money <= 30000:
     print("OK")
else:
    print("錢不夠")
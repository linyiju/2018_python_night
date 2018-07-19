def nine_mul():
    n = int(input("輸入一個數字，可以得到9*9法表："))
    i = 1
    j = 1 
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i*j < 10:
                print(i , "*" , j ,"= ",i*j, end = "  ")
            else:
                print(i , "*" , j ,"=", i*j , end ="  ")

        print(" ")
print("第一項：九九乘法表列印")
nine_mul()
# 作業一
def calculate():
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
print("第二項：四則運算")
calculate()
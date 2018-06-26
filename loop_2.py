#強制結束迴圈
#while 布林值：
#   break
#for 變數名稱 in 列表或字串：
#   break

##while sample 1 ##
n=1
while n < 5:
    if n==3:
        break
    n+=1
print(n)

#強制繼續下一圈
#while 布林值：
#   continue
#for 變數名稱 in 列表或字串：
#   continue

n=0
for x in [0,1,2,3,4,5,6,7]:
    if x % 2 == 0:
        continue
    n+=1
print(n)


#基本語法
#while 布林值
    #若布林值為True，執行命令
    #回到上方，做下一次的迴圈判斷
#else:
#   迴圈結束前，執行此區塊的命令

##while sample 2 ##
n=1
while n < 5 :
    print("變數n的資料是：",n)
    n+=1
else:
    print("變數n結束的資料是：",n)

##for sample 1 ##
for x in "Hello":
    print("逐一取出的字元為：",x)
else:
    print("最後取出的字元為：",x)

##else簡易版sample
sum = 0
for n in range(11):
    sum+=n
    print(n)
else:
    print(sum)


#綜合練習：找出整數平方根
#輸入9得到3
#11得到 沒有 整數的平方根
n = int(input("請輸入一個數值： "))
for i in range(n): #i 到 n-1 
    if i * i ==n:
        print("整數平方根為：",i)
        break
else:
    print("沒有整數平方根")

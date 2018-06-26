#while 迴圈
# while 布林值：
    #若布林值為True，執行命令。
    #回到上方，做下一次的迴圈判斷
#while_sample
n=1
while n<5:
    print("變數n的資料是:",n)
    n+=1
    break ＃立刻中止迴圈
n=1
while n <5:
    n+=1
    if n%2 == 0:
        continue #立即進入下一個迴圈
    print(n)
print("Final",n)
#for 迴圈
#for 變數名稱 in 列表或字串：
    #將列表中的項目或字串中的字源逐一取出，逐一處理
#for列出串列
for x in [3,5,1]:
    print("逐一列印出x的資料是:",x)
for列出字元
for c in "Hello":
    print("逐一列印出x的字元是:",c)

#for 變數名稱 in range(3):
#相當於
#for 變數名稱 in [0,1,2]:

#for 變數名稱 in range(3,6):
#相當於
#for 變數名稱 in [3,4,5]:


##while迴圈練習：1+2+..+50
sum = 0 #紀錄最後加總的結果
n = 1 #在迴圈中追蹤1,2,3,.....,50
while n <=50:
    print(n,sum)
    sum =sum+n #將n的數字累加進sum裡面
    n+=1
print(sum)

##for迴圈練習：1+2+..+10
sum = 0 
for x in range(1,11):
    sum = sum + x
print (sum)
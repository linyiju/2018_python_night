####函式參數詳解####
##基本語法##
#def 函式名稱(參數名稱=預設資料):
#   函式內部的程式碼


#參數msg預設資料為"Hello"
def say(msg="Hello"):
    print(msg)
say("Hello Function") #印出Hello Function
say() #印出Hello

#名稱對應
#def 函式名稱(名稱1,名稱2):
#   函式內部的程式碼

#呼叫函式，以參數名稱對應資料
#函式名稱(名稱2=3,名稱1=5)


#定義一個可以做除法的函式
def divide(n1,n2):
    result = n1/n2
    print(result)
divide(2,4)
divide(n2=2,n1=4)


#無限參數
#def 函式名稱(*無限參數):
#   無限參數以Tuple資料型態處理
#   函式內部的程式碼

#呼叫函式，可傳入無限數量的參數
#函式名稱(資料一,資料二,資料三)

#函式接受無限參數msgs
def speak(*messages):
    #以Tuple的方式處理
    for msg in messages:
        print(msg)
speak("Hello","World","HaHa")

def power(base,exp=0):
    print(base**exp)
power(3,2)
power(4)

#無限參數
def avg(*ns):
    sum = 0
    for n in ns:
        sum = sum+n
    result = sum /len(ns)
    print(result)

avg(3,4)
avg(1,2,3,4)
avg(-1,-4,5,0)
#基本函式語法
#def 函式名稱（參數名稱):
    #函式內部的程式碼

#定義一個印出Hello的函式
def sayHello():
    print("Hello")
#呼叫上方定義的函式
sayHello()

#定義可以印出任何訊息的函式
def say(msg):
    print(msg)
#呼叫上方定義的函式
say("Hello Function")

#定義一個可以做加法的函式
def add(n1,n2):
    result = n1+n2
    print(result)
add(1,4)



#基本語法-回傳值
#def 函式名稱（參數名稱):
    #函式內部的程式碼
    #return #結束函式，回傳None

#def 函式名稱（參數名稱):
    #函式內部的程式碼
    #return 資料 #結束函式，回傳「資料」  資料：數字、字串、布林值


#sample 2
def say(msg):
    print(msg)
    return
# #呼叫上方定義的函式
value = say("Hello")
print(value)

# #函式回傳字串Hello
def add(n1,n2):
    result = n1+n2
    return "Hello"
# #呼叫函式，取得回傳值    
value=add(1,4)
print(value)#印出Hello

# #函式回傳n1+n2的結果
def add(n1,n2):
    result = n1+n2
    return result
#呼叫函式，取得回傳值    
value=add(1,4)
print(value)#印出5

#定意函式
#函式內部的程式碼，若是沒有做函式呼叫，就不會執行
def multiply(n1,n2):
    # print(n1*n2)
    return n1 * n2
#呼叫函式
value = multiply(3,4) + multiply(5,10) #(3*4)+(5*10)
print(value)

# 程式的包裝
def calculate(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    print(sum)
calculate(10)
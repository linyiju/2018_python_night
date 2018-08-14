# 使⽤者可以輸⼊任意整數 n當輸⼊的n不為整數，提⽰使⽤者輸⼊型態錯誤，
# 並且重新讓使⽤者繼續輸⼊，若輸⼊的值為整數，將其print⾄螢幕上
n = input("請輸入一個正整數字：")
while n.isnumeric() == False:
    n = input("請再輸入一次:")
    continue
else:
    print("輸入正確")
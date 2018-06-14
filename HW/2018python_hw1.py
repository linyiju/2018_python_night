# 20180611 
# HW1 1.讓使用者輸入5個數字 2.告訴人家哪個數字最大 3.輸入數字總合多少
# Note: 使用List 列表處理
n1 = int(input("Enter a Number:"))
n2 = int(input("Enter a Number:"))
n3 = int(input("Enter a Number:"))
n4 = int(input("Enter a Number:"))
n5 = int(input("Enter a Number:"))

result = [n1,n2,n3,n4,n5]
print("輸入的數值:",result)
print("最大值:",max(result))
print("最小值:",min(result))
print("總和:",sum(result))
print("平均值：",sum(result)/len(result))

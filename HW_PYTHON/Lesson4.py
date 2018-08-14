# 函式Sample 1
# 輸入一個數字n，計算1+2+3+...+n的總和為多少?
def calculate(n):
    sum = 0
    for i in range(n+1):
        sum += i
    print(sum)
    return sum

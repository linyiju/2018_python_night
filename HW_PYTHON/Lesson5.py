# -*- coding: UTF-8 -*-

# #??????�?�???��??hello.txt???�?並寫??��??Hello World!???
# file=open("hello.txt","w",encoding="utf-8")
# a = input("�?輸�?��??�?輸�?��?????�?�?")
# file.write(a)
# # file.close()
# file.read()

# import pandas as pd

# data = pd.read_csv('stores_old.csv',encoding = 'big5')
# print(data.head())

# import csv

# with open('stores_old.csv', 'r', encoding = 'big5') as file:
#     data = file.read()
#     # print(type(data))
#     print(data)

# import csv
# with open("stores_old.csv","r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
# csvfile = open("stores_old.csv","rb")
# print(csvfile)
import csv

with open('stores_old.csv', 'r', encoding = 'big5') as file:
    reader = csv.reader(file)
    data = [row for row in reader]
    print(data)
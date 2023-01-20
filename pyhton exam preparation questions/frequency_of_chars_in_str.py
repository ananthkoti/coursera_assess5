# def char_frequency(str1):
#     dict = {}
#     for n in str1:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n] = 1
#     return dict
# print(char_frequency('google.com'))

import numpy as np
m , n = 4, 4       
def row_sum(arr) :
 
    sum = 0
 
    print("\nFinding Sum of each row:\n")
    for i in range(m) :
        for j in range(n) :
            sum += arr[i][j]
        print("Sum of the row",i,"=",sum)
        sum = 0
def column_sum(arr) :
 
    sum = 0
 
    print("\nFinding Sum of each column:\n")
    for i in range(m) :
        for j in range(n) :
            sum += arr[j][i]
        print("Sum of the column",i,"=",sum)

        sum = 0
def diagonal_sum(arr):
    Matrix=[[0]*m]*n
    sum=0
    for i in range(m):
     for j in range(m):
        if i==j:
            sum=sum+Matrix[i][j]
        elif i+j==m-1:
            sum=sum+Matrix[i][j]
print(sum)
if __name__ == "__main__" :
 
    arr = np.zeros((4, 4))
    x = 1
     
    for i in range(m) :
        for j in range(n) :
            arr[i][j] = x
 
            x += 1
    row_sum(arr)
    column_sum(arr)

    
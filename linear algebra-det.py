import numpy as np
arr=[]
n=int(input())
for _ in range(n):
    a=list(map(float,input().split()))
    arr.append(a)
print(round(np.linalg.det(arr),2))
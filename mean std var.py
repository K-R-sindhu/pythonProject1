import numpy as np
arr=[]
n,m=map(int,input().split())
for _ in range(n):
    a=list(map(int,input().split()))
    arr.append(a)
print(np.mean(arr,axis=1))
print(np.var(arr,axis=0))
print(round(np.std(arr),11))
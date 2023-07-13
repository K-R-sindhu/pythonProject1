
import numpy as np
N, M = map(int, input().split())
arr = []
for i in range(N):
    f = list(map(int, input().split()))
    arr.append(f)

a=np.min(arr,axis=1)
b=set(a)
print(max(b))
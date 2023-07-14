from itertools import *
n=int(input())
b=input().split()
k=int(input())
count=0
for i in list(combinations(b,k)):
    if "a" in i:
        count+=1
print(count/len(list(combinations(b,k))))
# your code goes here
a=list(map(int,input().split()))
l=list(map(int,input().split()))
s=0
for i in range(a[1]):
    s+=l[i]
print(s)
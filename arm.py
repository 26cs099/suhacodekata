n=input()
a=len(n)
n=int(n)
t=n
r=f=0
while n>0:
    r=n%10
    f=f+r**a
    n=n//10
if t==f:
    print("yes")
else:
    print("no")
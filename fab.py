# your code goes here
n=int(input())
a=0
b=1
while(n>0):
	print(b,end=" ")
	a,b=b,a+b
	n=n-1

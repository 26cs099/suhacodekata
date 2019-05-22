# your code goes here
a=int(input())
t=a
rev=0
while(a>0):
	rev=(rev*10)+(t%10)
	a=a//10
if(t==rev):
	print("yes")
else:
	print("no")
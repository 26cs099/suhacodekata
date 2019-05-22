# your code goes here
n=int(input())
t=n
rev=0
while(n>0):
	rev=(rev*10)+(t%10)
	n=n//10
if(t==rev):
	print("yes")
else:
	print("no")

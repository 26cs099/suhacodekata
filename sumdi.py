a=int(input())
sum=0
n=0
while(a>0):
	n=a%10
	sum=n+sum
	a=a//10
print(sum)
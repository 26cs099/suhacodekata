# your code goes here
m,n=map(str,input().split())
cost=abs(len(m)-len(n))
for j in range(len(m)):
	if(len(m)==1 and m[j] in n):
		break
	if(m[j] != n[j]):
		cost+=1
print(cost)
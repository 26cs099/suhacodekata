# your code goes here
s,m=map(str,input().split())
cost=abs(len(s)-len(m))
for k in range(len(s)):
	if(len(s)==1 and s[j] in m):
		break
	if(s[j] != m[j]):
		cost+=1
print(cost)

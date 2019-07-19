# your code goes here
s,m=map(str,input().split())
costset=abs(len(s)-len(m))
for k in range(len(s)):
	if(len(s)==1 and s[j] in m):
		break
	if(s[j] != m[j]):
		costset+=1
print(costset)

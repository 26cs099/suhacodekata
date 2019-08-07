
# your code goes here
n=int(input())
s=[]
for i in range(1,n+1):
	if(i%2==0):
		s.append(i)
print(s)
for j in range(1,len(s)):
	if(s[j]==n):
		print(s[j])
	elif(s[j]==n-1):
		print(s[j])
	else:
		j+=1
	
	
		
	

# your code goes here
n=int(input())
s=[]
for k in range(n):
	c=input()
	s.append(c)
d=[]
for k in zip(*s):
	if(k.count(k[0])==len(k)):
		d.append(k[0])
	else:
		break
print("".join(d))
	
# your code goes here
g=int(input())
h=list(map(int,input().split()))
i=0
for k in range(g):
	for l in range(k,g):
		for t in range(l,g):
			if(h[k]<h[l]<h[t]):
				i+=1
print(i)

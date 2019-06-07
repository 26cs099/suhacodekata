a,b=input().split()
a=int(a)
b=int(b)
for n in range(a,b):
     c=0
     d=n
     while(n!=0):
          r=n%10
          c=c+r*r*r
          n//=10
     if(d==c):
        print(d,end=" ")
	  

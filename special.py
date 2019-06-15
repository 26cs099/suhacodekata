# your code goes here
n=str(input())
sum=0
for i in range(len(n)):
	if(n[i].isnumeric()==False and n[i].isalpha()==False and n[i].isspace()==False):
		sum=sum+1
print(sum)
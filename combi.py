# your code goes here
from itertools import combinations
h,s=map(int,input().split())
d=len(str(h))
l=list(combinations(str(h),d-s))
l=sorted(l)
print("".join(l[0])

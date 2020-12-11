import os
from collections import defaultdict
numbers=[]
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),__file__.replace('.py','.in')),'r',encoding='utf8') as f:
    for l in f:
        numbers.append(int(l.strip()))

last=0
diffs=defaultdict(int)
diffs[3]=1
numbers.sort()
streak=0
combos=1
numbers=[0]+numbers+[numbers[-1]+3]
for n in numbers:
    diff=n-last
    diffs[diff]+=1
    if diff==1:
        streak+=1
    if diff==3:
        if streak-1==1:
            combos*=2
        if streak-1==2:
            combos*=4
        if streak-1==3:
            combos*=7
        streak=0
    last=n
#print (numbers)
#print (diffs)
print(diffs[1]*diffs[3])
print(combos)
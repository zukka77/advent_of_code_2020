import os
from  itertools import combinations
from functools import reduce
WINDOW=25


numbers=[]
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),__file__.replace('.py','.in')),'r',encoding='utf8') as f:
    for l in f:
        numbers.append(int(l.strip()))

#print (numbers)
preamble=numbers[:WINDOW]
invalid=None
for i in range(WINDOW,len(numbers)):
    if numbers[i] not in [x+y for x,y in combinations(preamble,2)]:
        invalid=numbers[i]
        break
    preamble.pop(0)
    preamble.append(numbers[i])

print (invalid)
#PART2
terms=[]
key=None
for n in numbers:
    terms.append(n)
    sum=reduce(lambda a,e:a+e,terms,0)
    if sum == invalid and len(terms)>1:
        key=min(terms)+max(terms)
        break
    elif sum<invalid:
        continue
    else:
        while sum>invalid:
            sum-=terms.pop(0)
        if sum==invalid and len(terms)>1:
            key=min(terms)+max(terms)
            break

print(key)


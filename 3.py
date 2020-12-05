
from functools import reduce

with open('3.in','r',encoding='utf8') as f:
    treemap=[]
    for l in f:
        treemap.append(l.strip())


linesize=len(treemap[0])
res=[]
moves=[
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2),
]
for m in moves:
    ntrees=0
    x=0
    y=0
    while y<len(treemap):
        if treemap[y][x%linesize]=='#':
            ntrees+=1
        x+=m[0]
        y+=m[1]
    res.append(ntrees)
print(res)
print (reduce(lambda a,e: a*e,res))
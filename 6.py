import os
from functools import reduce

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),__file__.replace('.py','.in')),'r',encoding='utf8') as f:
    s=0
    e=0
    group_answers=set()
    user_answers=[]
    for l in f:
        l=l.strip()
        if not l:
            s+=len(group_answers)
            e+=len(reduce(lambda a,e: a&e,user_answers,group_answers))
            group_answers=set()
            user_answers=[]
            continue
        group_answers.update(l)
        user_answers.append(set(l))

print (f"{s} {e}")
        
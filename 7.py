import os
from collections import defaultdict

def find_container(color,contained,found):
    found.add(color)
    for c in contained[color]:
        found.update(find_container(c,contained,found))
    return found

def find_bags(container,containers,n=0):
    nc=1
    for c in containers[container]:
        nc+=c['q']*find_bags(c['color'],containers,0)
    return n+nc

contained=defaultdict(set)
containers=defaultdict(list)
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),__file__.replace('.py','.in')),'r',encoding='utf8') as f:
    for l in f:
        #dull magenta bags contain 3 dull lime bags, 2 light gold bags, 2 striped purple bags.
        if "contain no other bags." in l:
            continue
        container,rest=l.strip().split(' bags contain ')
        container=container.strip().replace(' ','_')
        for r in rest[:-1].split(','):
            q,color=r.strip().replace(' bags','').replace(' bag','').split(' ',1)
            color=color.replace(' ','_')
            containers[container].append({"color":color,"q":int(q)})
            contained[color].add(container)
n_bags=0



good_container=find_container('shiny_gold',contained,set())-{'shiny_gold'}
print(len(good_container))
print(find_bags('shiny_gold',containers)-1)

            

import os
from collections import namedtuple

Dir=namedtuple('Dir',['command','value'])

class Ship:
    def __init__(self,nav,wp=[0,0]):
        self.heading=90
        self.position=[0,0]
        self.nav=nav
        self.wp=wp
    
    def distance(self):
        return abs(self.position[0])+abs(self.position[1])
        
    def navigate(self):
        for n in nav:
            if n.command=='N' or ( n.command=='F' and self.heading==0) :
                self.position[1]+=n.value
            elif n.command=='E' or  ( n.command=='F' and self.heading==90):
                 self.position[0]+=n.value
            elif n.command=='S' or ( n.command=='F' and self.heading==180):
                self.position[1]-=n.value
            elif  n.command=='W' or ( n.command=='F' and self.heading==270):
                self.position[0]-=n.value
            elif n.command=='R':
                self.heading=(self.heading+n.value)%360
            elif n.command=='L':
                self.heading=(self.heading-n.value)%360
    
    def navigate_wp(self):
        for n in nav:
            if n.command=='N':
                self.wp[1]+=n.value
            elif n.command=='E':
                 self.wp[0]+=n.value
            elif n.command=='S':
                self.wp[1]-=n.value
            elif  n.command=='W':
                self.wp[0]-=n.value
            elif n.command=='R':
                for _ in range(n.value//90):
                    self.wp=[self.wp[1],-self.wp[0]]
            elif n.command=='L':
                for _ in range(n.value//90):
                    self.wp=[-self.wp[1],self.wp[0]]
            elif n.command=='F':
                self.position=[self.position[0]+self.wp[0]*n.value,self.position[1]+self.wp[1]*n.value]
                #self.wp=[self.position[0]+self.wp[0],self.position[1]+self.wp[1]]
            #print (f"command: {n} position: {self.position} wp: {self.wp}")
nav=[]
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),__file__.replace('.py','.in')),'r',encoding='utf8') as f:
    for l in f:
        l=l.strip()
        nav.append(Dir(l[0],int(l[1:])))

print (nav)
s=Ship(nav=nav)
s.navigate()
print(s.distance())
s=Ship(nav=nav,wp=[10,1])
s.navigate_wp()
print(s.distance())
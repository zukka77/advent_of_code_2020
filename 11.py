import os
from collections import defaultdict
from copy import deepcopy

def print_seats(s):
    for l in s:
        print("".join(l))

def n_occupied(seats,x,y):
    n=0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i==x and j==y:
                continue
            if seats[i][j]=='#':
                n+=1
    return n

def n_occupied_all(seats,x,y):
    n=0
    #up
    i=x-1
    while i >0:
        if seats[i][y]=='L':
            break
        if seats[i][y]=='#':
            n+=1
            break
        i-=1
    #down
    i=x+1
    while i <len(seats):
        if seats[i][y]=='L':
            break
        if seats[i][y]=='#':
            n+=1
            break
        i+=1
    #left
    j=y-1
    while j >0:
        if seats[x][j]=='L':
            break
        if seats[x][j]=='#':
            n+=1
            break
        j-=1
    #right
    j=y+1
    while j <len(seats[0]):
        if seats[x][j]=='L':
            break
        if seats[x][j]=='#':
            n+=1
            break
        j+=1
    #ul
    i=x-1
    j=y-1
    while i >=0 and j >=0:
        if seats[i][j]=='L':
            break
        if seats[i][j]=='#':
            n+=1
            break
        i-=1
        j-=1
    #ur
    i=x-1
    j=y+1
    while i >=0 and j <len(seats[0]):
        if seats[i][j]=='L':
            break
        if seats[i][j]=='#':
            n+=1
            break
        i-=1
        j+=1
    #dl
    i=x+1
    j=y-1
    while i <len(seats) and j >=0:
        if seats[i][j]=='L':
            break
        if seats[i][j]=='#':
            n+=1
            break
        i+=1
        j-=1
    #dr
    i=x+1
    j=y+1
    while i <len(seats) and j <len(seats[0]):
        if seats[i][j]=='L':
            break
        if seats[i][j]=='#':
            n+=1
            break
        i+=1
        j+=1
    return n


def count_occupied(s):
    n=0
    for i in s:
        for j in i:
            if j == '#':
                n+=1
    return n

def count_occupied_all(s):
    n=0
    for i in s:
        for j in i:
            if j == '#':
                n+=1
    return n

seats=[]
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),__file__.replace('.py','.in')),'r',encoding='utf8') as f:
    for l in f:
        l=l.strip()
        seats.append(['.']+[x for x in l]+['.'])
filler_row=['.' for _ in range(len(seats[0]))]
seats=[filler_row]+seats
seats.append(filler_row)

last=seats

while True:
    res=deepcopy(last)
    for x in range(1,len(seats)-1):
        for y in range(1,len(seats[0])-1):
            if last[x][y]=='.':
                continue
            if last[x][y]=='L' and n_occupied(last,x,y)==0 :
                res[x][y]="#"
                continue
            if last[x][y]=='#' and n_occupied(last,x,y)>=4 :
                res[x][y]="L"
                continue
    if last==res:
        break
    last=res

fst_last=last

last=seats

while True:
    res=deepcopy(last)
    for x in range(1,len(seats)-1):
        for y in range(1,len(seats[0])-1):
            if last[x][y]=='.':
                continue
            if last[x][y]=='L' and n_occupied_all(last,x,y)==0 :
                res[x][y]="#"
                continue
            if last[x][y]=='#' and n_occupied_all(last,x,y)>=5 :
                res[x][y]="L"
                continue
    #if is_identical(last,res):
    if last==res:
        break
    last=res


#print_seats(fst_last)
print(count_occupied(fst_last))
#print_seats(last)          
print(count_occupied(last))
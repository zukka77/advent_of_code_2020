

def get_seat_id(code:str)->int:
    rowl=128
    coll=8
    row=0
    col=0
    for r in code[:7]:
        rowl//=2
        if r=='B':
            row+=rowl
    for c in code[7:]:
        coll//=2
        if c=='R':
            col+=coll
    return row*8+col

seat_ids=[]
with open('5.in','r',encoding='utf8') as f:
    for l in f:
        seat_ids.append(get_seat_id(l.strip()))
        seat_ids.sort()
        for i in range(1,len(seat_ids)):
            if seat_ids[i]-seat_ids[i-1]!=1:
                my_seat=seat_ids[i]-1


print (f"max_seat_id: {seat_ids[-1]} my seat: {my_seat}")

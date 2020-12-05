


def get_seat_id(code:str)->tuple:
    row=[0,127]
    col=[0,7]
    for r in code[:7]:
        if r=='F':
            row[1]=(row[1]+row[0])//2
        else:
            row[0]=(row[1]+row[0])//2+1
    for c in code[7:]:
        if c=='L':
            col[1]=(col[1]+col[0])//2
        else:
            col[0]=(col[1]+col[0])//2+1

    #print(row[0],col[0],row[0]*8+col[0])
    return row[0]*8+col[0]


seat_ids=[]
with open('5.in','r',encoding='utf8') as f:
    for l in f:
        seat_ids.append(get_seat_id(l.strip()))
        seat_ids.sort()
        for i in range(1,len(seat_ids)):
            if seat_ids[i]-seat_ids[i-1]!=1:
                my_seat=seat_ids[i]-1


print (f"max_seat_id: {seat_ids[-1]} my seat: {my_seat}")

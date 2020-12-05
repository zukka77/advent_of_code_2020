


with open('2.in','r',encoding='utf8') as f:
    good=0
    verygood=0
    for l in f:
        low_high,letter,password=l.strip().split()
        letter=letter[0]
        low,high=low_high.split('-')
        count=password.count(letter)
        if count>=int(low) and count <= int(high):
            good+=1
        ll=password[int(low)-1]==letter 
        hl=password[int(high)-1]==letter
        if ll != hl:
            verygood+=1
print(good)
print(verygood)
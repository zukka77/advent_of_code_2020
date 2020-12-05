import re
def check_passport(data):
    must_data=[
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    ]
    opt_data=['cid']
    def hgt(x):
        m=re.search(r'(\d+)\s*(cm|in)',x)
        if not m:
            return False
        h=int(m.group(1))
        u=m.group(2)
        if u=='cm':
            return h>=150 and h<=193
        return h>=59 and h<=76
    validators={
        'byr': lambda x: int(x)>=1920 and int(x) <=2002,
        'iyr': lambda x: int(x)>=2010 and int(x) <=2020,
        'eyr': lambda x: int(x)>=2020 and int(x) <=2030,
        'hgt': lambda x: hgt(x),
        'hcl': lambda x: re.search(r'^#[\da-f]{6}$',x.strip()) != None,
        'ecl': lambda x: x in ('amb','blu','brn','gry','grn','hzl','oth'),
        'pid': lambda x: re.search(r'^\d{9}$',x.strip()) != None,
        'cid': lambda _: True,
    }
    good=True
    valid=True
    for k,v in data.items():
        if k not in must_data+opt_data:
            valid=False
            good=False
            break
        if not validators[k](v):
            #print (k)
            valid=False
    for k in must_data:
        if k not in data.keys():
            good=False
            valid=False
            break
    return good,valid

with open('4.in','r',encoding='utf8') as f:
    ndata=0
    nvalid=0
    data={}
    n=0
    for l in f:
        l=l.strip()
        if not l:
            good,valid=check_passport(data)
            nvalid+=1 if valid else 0
            ndata+=1 if good else 0
            #print(f"{data} {good} {valid}")
            data={}
            continue
        for d in l.split():
            k,v=d.split(':')
            data[k]=v
    good,valid=check_passport(data)
    nvalid+=1 if valid else 0
    ndata+=1 if good else 0

print(ndata,nvalid)
'''
inp : OQQSNPOQZBCETV NPSU SUNPRTJLHJ XZZB HJ KMDFMOHJ
out : PROPADU OT TOSKI YA I LENI

'''

import string as str

inp = list(input())
eng_alphabet = list(str.ascii_uppercase)

d = {eng_alphabet[a]:eng_alphabet[a+1] for a in range(25)}
d_t = {'Z' : 'A'," " : " "}
d.update(d_t)
a=0
while a<len(inp):
    if d[inp[a]]!=' ':
        print(d[inp[a]] ,end='')
        a+=2
    elif d[inp[a]]==' ':
        print(d[inp[a]] ,end='')
        a+=1
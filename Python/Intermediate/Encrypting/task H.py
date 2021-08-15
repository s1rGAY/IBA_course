'''
inp : 
3
LDPELJPDCCB

out : 
IAMBIGMAZZY

'''


import string as str

alphabet_eng =  list(str.ascii_uppercase)

step = int(input())
if step>=0:
    step*=-1
else :
    step=abs(step)
inp = list(input())

a=0
while a<len(inp):
    print(alphabet_eng[(step+alphabet_eng.index(inp[a]))%26],end='')
    a+=1

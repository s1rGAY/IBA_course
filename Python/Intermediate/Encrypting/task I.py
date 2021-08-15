'''
Формула шифрования: c_i = [(m_i + k_1)*k_2]mod26
inp : 
3
5
IAMBIGMAZZY

out : 
DPXUDTXPKKF

'''

import string as str

alphabet_eng =  list(str.ascii_uppercase)

step = int(input())
ind = int(input())

#if step>=0:
#    step*=-1
#else :
#    step=abs(step)
inp = list(input())

a=0
while a<len(inp):
    print(alphabet_eng[((alphabet_eng.index(inp[a])+step)*ind)%26],end='')
    a+=1
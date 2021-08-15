'''
Шифр Вижинера. Дешифрование
inp : 
BEAR
JEMSJKMRADY
out :
IAMBIGMAZZY
'''

import string as str
key = list(input())
inp = list(input())
alp =  list(str.ascii_uppercase)
for a in range(len(inp)):
    print(alp[(alp.index(inp[a])+26-alp.index(key[(a+len(key))%len(key)]))%26],end='')
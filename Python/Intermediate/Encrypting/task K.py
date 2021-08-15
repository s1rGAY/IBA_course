'''
Шифр Вижинера. Шифрование
Формат входных данных
В первой строке – ключ шифрования. Длина ключа не более 10 символов.
Во второй строке – открытый текст, записанный прописными буквами английского алфавита.
Длина открытого текста – до 10^5 символов.
Формат выходных данных
Зашифрованное сообщение.

inp : 
BEAR
IAMBIGMAZZY
out :
JEMSJKMRADY
'''

import string as str
key = list(input())
inp = list(input())
alphabet_eng =  list(str.ascii_uppercase+str.ascii_lowercase)
for a in range(len(inp)):
    print(alphabet_eng[(alphabet_eng.index(key[(a+len(key))%len(key)])+alphabet_eng.index(inp[a]))%26],end='')  
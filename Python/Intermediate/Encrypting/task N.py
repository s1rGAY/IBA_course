'''
Шифр блочной одинарной перестановки. Дешифрование
Формат входных данных
В первой строке – целое число N, количество столбцов таблицы перестановок блока символов.
В следующих N строках – неповторяющиеся целые числа от 0 до N-1 (элементы второй строки таблицы перестановок).
В последней строке – шифротекст. Длина открытого текста – до 10^5 символов.
Формат выходных данных
Расшифрованное сообщение.

inp : 
3
2
1
0
a_Ib_m_gizaM_yz
out : 
I_am_big_Mazzy_
'''


import string as st

keys = int(input())
txt=[[a for a in range(keys)],[a for a in range (keys)]]
for x in range(keys):
    txt[1][x]=int(input())
text=input()
anws = [str(x-x) for x in range(len(text))]
t_1=len(text)//keys
for x in range(t_1):
    for y in range(keys):
        anws[txt[1][y]]=text[txt[0][y]]
        txt[0][y]+=keys
        txt[1][y]+=keys
for i in range(len(anws)):
    print(anws[i],end='')
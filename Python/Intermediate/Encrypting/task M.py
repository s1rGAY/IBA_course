'''
Шифр блочной одинарной перестановки. Шифрование

Формат входных данных
В первой строке – целое число N, количество столбцов таблицы перестановок.
В следующих N строках – неповторяющиеся целые числа от 0 до N-1 (элементы второй строки таблицы перестановок).
В последней строке – открытый текст. Длина открытого текста – до 10^5 символов.
Формат выходных данных
Зашифрованное сообщение.

inp : 
3
2
1
0
I_am_big_Mazzy_
out : 
a_Ib_m_gizaM_yz
'''



inc = int(input())
txxList = [[x for x in range (inc)],[x for x in range(inc)]]
for i in range(inc):
    txxList[1][i]=int(input())
    
text=input()
dec_arr=[str(x-x) for x in range(len(text))]

for i in range (len(text)//inc):
    for j in range(inc):
        dec_arr[txxList[1][j]]=text[txxList[0][j]]
        txxList[0][j]+=inc
        txxList[1][j]+=inc
        
for i in range(len(dec_arr)):
    print(dec_arr[i], end='')
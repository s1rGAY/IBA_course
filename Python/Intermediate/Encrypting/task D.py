'''
Дана строка, содержащая сообщение, зашифрованное неизвестным алгоритмом. Расшифруйте это сообщение
Формат входных данных
Единственная строка, содержащая буквы английского алфавита. Длина строки – до 10^3 символов.
Формат выходных данных
Расшифрованное сообщение.

inp : PBZCHGRE FPVRAPR
out : COMPUTER SCIENCE
'''

A0 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
A1 = 'NOPQRSTUVWXYZABCDEFGHIJKLM'
k = -13
M = input()
CN = {chr(i):i-ord('A') for i in range(ord('A'), ord('Z')+1)}
NC = {i-ord('A'):chr(i) for i in range(ord('A'), ord('Z')+1)}
print ("".join([NC[(CN[m] + k) % 26] if m in A0 else m for m in M]))
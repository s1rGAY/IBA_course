'''
Дана строка в кодировке cp1251cp1251. Представьте ее содержимое в hexhex-формате
Формат входных данных
Строка символов в кодировке cp1251cp1251
Формат выходных данных
Строка 16-ирчных символов
'''
import binascii
str=input().encode('cp1251')
print(binascii.hexlify(bytes(str)))

#s = input()
#print ("".join([hex(ord(c))[2:] for c in s]))
#s=input().encode('cp1251')
#print("".join([hex(c)[2:] for c in s]))
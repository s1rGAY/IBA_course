'''
Дана строка, содержащая сообщение, зашифрованное неизвестным алгоритмом. Расшифруйте это сообщение.
Given a string containing a message, encrypted by an unknown algorithm. Decipher this message.
Формат входных данных
Единственная строка, содержащая латинские буквы. Длина строки – до 10^3 символов.
The line containing only LATIN letters (an alphabet of 26 letters). The length of this line is up to 10^3 characters. 
All characters are small, without spaces.
Формат выходных данных
Расшифрованное сообщение.
Decrypted message.

example : 
inp : Veguhe Xbana Yblyr Our Cbhaq bs gur Wnfxreivyyrf ze Nureybpx Cbyzrf
out : Arthur Conan Doyle The Hound of the Baskervilles mr Sherlock Holmes

'''

import string as str

inp = input()

low_eng_alphabet = list(str.ascii_lowercase)
up_eng_alphabet = list(str.ascii_uppercase)

d_u={up_eng_alphabet[a] : up_eng_alphabet[a+5] for a in range(21)}
t_du={up_eng_alphabet[21+a] : up_eng_alphabet[a] for a in range(5)}
d_u.update(t_du)

d_l={low_eng_alphabet[a] : low_eng_alphabet[a+13] for a in range(13)}
t_dl = {low_eng_alphabet[13+a] : low_eng_alphabet[a] for a in range(13)}
d_l.update(t_dl)

d_all = {" ": " "}
d_all.update(d_l)
d_all.update(d_u)

for v in range(len(inp)):
    print(d_all[inp[v]],end='')
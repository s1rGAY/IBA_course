'''
Дана строка, содержащая сообщение, зашифрованное неизвестным алгоритмом. На основе шифров, приведенных в качестве примера, укажите, как будут зашифрованы входные данные задачи. Можно отметить, исходный текст набран в латинском алфавите, состоящем из 26 букв.
Given a string containing a message, encrypted by an unknown algorithm. Based on the ciphertexts provided as an example, specify how the input data of the task will be encrypted. The source text is typed in the latin alphabet, consisting of 26 letters.
Формат входных данных
В первой строке – число MM – количество строк, которые надо зашифровать.
Далее идут MM строк, содержащих исходный текст.
In the first line – the integer M - the number of lines that need to be encrypted.
Then there are M lines containing the source text.
Формат выходных данных
В первой строке – шифр для первой введенной строки.
Во второй строке – шифр для второй введенной строки.
В MM-й строке – шифр для MM-й введенной строки.
The first line contains the ciphertext for the first input line.
The second line contains the ciphertext for the second input line.
The M-th line contains the ciphertext for the M-th input line.

inp : 
4
CRYPTOGRAPHY
CIPHER
ENIGMA
HRODNA

out : 
31225
3618
561
861

'''

import string as str
i = int(input())
while i:

    inp = list(input())
    eng_alphabet = list(str.ascii_uppercase)
    d={eng_alphabet[a] : a+1 for a in range(26)}
    print(d[inp[0]],end="")
    print(len(inp),end="")
    print(d[inp[len(inp)-1]])
    i-=1


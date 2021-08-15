'''
inp : QPMQBES MU UMTLG ZB G JFOG
out : PROPADU OT TOSKI YA I LENI
'''


import string as str

inp_str = list(input())
alphabet = str.ascii_uppercase
d = {alphabet[0]:'C',alphabet[1]:'A',alphabet[2]:'B',alphabet[3]:'F',
    alphabet[4]:'D',alphabet[5]:'E',alphabet[6]:'I',alphabet[7]:'G',
    alphabet[8]:'H',alphabet[9]:'L',alphabet[10]:'J',alphabet[11]:'K',
    alphabet[12]:'O',alphabet[13]:'M',alphabet[14]:'N',alphabet[15]:'R',
    alphabet[16]:'P',alphabet[17]:'Q',alphabet[18]:'U',alphabet[19]:'S',
    alphabet[20]:'T',alphabet[21]:'X',alphabet[22]:'V',alphabet[23]:'W',
    alphabet[24]:'Z',alphabet[25]:'Y'," ":" "}

for v in range(len(inp_str)):
    print(d[inp_str[v]],end='')
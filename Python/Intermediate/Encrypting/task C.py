


import string as str

text = str.ascii_lowercase
indecies = [text]
values = (text.count(letter) for letter in indecies)
analize = dict(zip(indecies, values))
print(analize)
#d={a: str.ascii_lowercase(a) for a in range(26)}
#print(d)

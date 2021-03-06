'''
При написании текста курсовой работы студент по ошибке неверно оформил ссылки на цитируемые источники.
Примером такой ошибки может быть строка:
" ... этот метод активно обсуждался в работах. [1,12,19-23] ..."
которую надо переделать в
" ... этот метод активно обсуждался в работах [1,12,19-23]. ..."
Используя регулярные выражения, выполните замену ошибочного оформления на правильное.
Помните ! Каждый пробел важен !!!
Формат входных данных
Непустая строка
Формат выходных данных
Исправленная строка
'''
import re

s = input()

sh =  re.compile(r'(\.)( )(\[[0-9,-]+\])')
result = sh.sub(r'\2\3\1',s)
print (result)

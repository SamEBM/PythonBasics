# Regular Expression 101
import re

patron = re.compile(r"([a-zA-Z]).([a])")        # Va a buscar una cadena que contenga cualquier valor alfabetico, seguido de algo y despues una "a"
cadena = 'Buscar algo en este texto con algo'

a = patron.search(cadena)
print(a.group())

b =  patron.findall(cadena)
print(b)
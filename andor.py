# OPERATORY LOGICZNE
# and - logiczne 'i' - kazdy jeden musi byc spelniony
# or - logiczne 'lub' - wystarczy jeden zeby warunek byl spelniony
# ^ - xor - logiczne 'albo' - tylko jeden warunek musi byc spelniony

a = 'Piotr'
b = ''
print(b and a)  #-> false, i zwraca to co 
print(a or b)
# print(a ^ b)
print(bool(a and b))
print(bool(a or b))



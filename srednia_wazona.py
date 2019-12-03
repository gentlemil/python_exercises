# waga = [1,2,3]
# marks1 = [1,2,3]
# marks2 = [1,2,3]
# marks3 = [1,2,3]
# suma1 = 0
# suma2 = 0
# suma3 = 0

# for i in marks1:
#     suma1 += i
# for i in marks2:
#     suma2 += i
# for i in marks3:
#     suma3 += i

# SUMA = ( (suma1*waga[0])+(suma1*waga[1])+(suma1*waga[2]) )/(waga[0]*waga[1]*waga[2])
# print(SUMA)

# --------------------------------------
liczby = [1,2,3,4,5,6,7]
wagi = [1,1,1,2,2,3,2]
licznik = 0
mianownik = 0

# I SPOSOB
for i in range(len(wagi)):
    licznik += liczby[i] * wagi[i]
    mianownik += wagi[i]
print(licznik/mianownik)

# II SPOSOB -  LEPSZY, IDIOMATYCZNY! ZIP - zamek blyskawiczny
for liczba, waga in zip(liczby,wagi):
    licznik += liczba * waga
    mianownik += waga
print(licznik/mianownik)
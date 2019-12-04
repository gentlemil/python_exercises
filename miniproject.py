# I SPOSOB
# komputer losuje liczbe z zakresu 1-100
# czlowiek musi zgadnac korzystajac ze wskazowek komputera jaka to liczba
# wylosowanie liczby
# import random
# liczba = random.randint(1,100)
# petla glowna program (for in range (1,7) albo while z flaga zgadnietej liczby, while z dwoma warunkami (uzyt. nie wykorzystal ))
#  w glownej petli brac input > < == feedback 
# wygrywa jesli zgadl w 7 probach, inaczej pzregral

# II SPOSOB
# komputer probuje zgadnac to co my sobie wymyslilismy

# --------------------------------------------------------------------
# ----------- I SPOSOB - LOSUJEMY CO KOMPUTER WYLOSOWAL --------------
# import random
# randomNumber = random.randint(1, 100)
# def guessNumber():
#     for i in range(1,8):
#         yourGuess = int(input('PODAJ LICZBE: '))
#         if yourGuess > randomNumber and yourGuess > 0:
#             print('PODAJ MNIEJSZA LICZBE')
#         elif yourGuess < randomNumber and yourGuess > 0:
#             print('PODAJ WIEKSZA LICZBE')
#         elif yourGuess == randomNumber:
#             print('GRATULUJE, ZGADLES ZA', i, 'RAZEM!')
#             break
#         else:
#             print('LICZBA Z POZA PRZEDZIALU 1-100.')

# print('HEJ! WYLOSOWALEM DLA CIEBIE LICZBE Z PRZEDZIALU 1-100.')
# answer = (input('CZY CHCESZ SPROBOWAC ZGADNAC CO TO ZA LICZBA (y/n)? ')).lower()

# if answer == 'y':
#     print(guessNumber())
# elif answer == 'n':
#     print('Dziekujemy za uwage, papa!')
# else:
#     print("Wpisz 'y' (yes) albo 'n' (no).")

# --------------------------------------------------------------------
# ----------- II SPOSOB - KOMPUTER ZGADUJE NASZA LICZBE --------------
import random
# randomNumber = random.randint(1, 100)
def whatsYourNumber():
    randomNumber = random.randint(1, 100)
    for i in range(1,8):
        print('CZY TO BEDZIE LICZBA', randomNumber, '?')
        if str(input('')).lower() == 'y':
            print('YAAY! ALE JESTEM MADRY! :))')
        elif str(input('')).lower() == 'n':
            print('OKEY. CZY TO BEDZIE WIEKSZA LICZBA?')
            if str(input('')).lower() == 'y':
                randomNumber = random.randint(randomNumber, randomNumber)
            elif str(input('')).lower() == 'n':
                randomNumber = random.randint(randomNumber, randomNumber)
            else:
                print('NIE OSZUKUJ PROSZE, BO SIE GUBIE')

print('HEJ! WYMYSL LICZBE Z PRZEDZIALU 1-100 A JA JA ZGADNE W 7 PROBACH.')
answer = (input('ZACZYNAMY (y/n)? ')).lower()

if answer == 'y':
    print(whatsYourNumber())
elif answer == 'n':
    print('Dziekujemy za uwage, papa!')
else:
    print("Wpisz 'y' (yes) albo 'n' (no).")
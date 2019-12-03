# III SPOSOBY na liczenie literek w tekscie:
# 1. liczenie + slownik + warunki jw.
# 2. defaultdict
# 3. collections.defaultdict
# 4. collections.Counter

tekst = 'loremipsumsitdolor'
slownik = {}
for literka in tekst:
    if literka in tekst:
        slownik[literka] += 1
    else:
        slownik[literka] = 1

# from collections import Counter
# print(Counter(tekst))

# from collections import defaultdict
# slownik = defaultdict(int)
# for literka in tekst:
#     slownik[literka] += 1
# print(slownik)
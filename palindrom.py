word = "atujakatakajutaaaaa"
# word = 'kayak'

for i in range(0, len(word)):
    if word[i] == word[len(word) - i - 1]:
        print('JEST')
        break
    else:
        print('to NIE JEST palindrom')
        break

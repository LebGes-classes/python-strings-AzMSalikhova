import re

text = input("Введите текст: ")

words = re.findall(r'\b[а-яa-zё]+\b', text.lower())
dict_words = {}


for word in words:
    if word in dict_words:
        dict_words[word] += 1
    else:
        dict_words[word] = 1

list_words = []

for word in dict_words:
    list_words.append({word: dict_words[word]})

n = len(list_words)

for i in range(n):
    for j in range(n - 1):
        value_j = list(list_words[j].values())[0]
        value_j1 = list(list_words[j + 1].values())[0]

        if value_j < value_j1:
            list_words[j], list_words[j + 1] = list_words[j + 1], list_words[j]

until5 = 0
print('Топ - 5 самых частых слов: ')

for item in list_words:
    if until5 < 5:
        key = list(item.keys())[0]

        print(until5 + 1, ' - ', key)

        until5 += 1

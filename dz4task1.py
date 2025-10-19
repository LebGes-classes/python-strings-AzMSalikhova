text = input('Введите текст: ')

words = []
current_word = ''

for symbol in text:
    if symbol == ' ':
        words.append(current_word)
        current_word = ''
    else:
        current_word += symbol

if current_word:
    words.append(current_word)

length_words = len(words)
mirror_text = ''

for j in range(length_words - 1, -1, -1):
    mirror_text += words[j]
    if j > 0:
        mirror_text += ' '

reversed_text = ''
length_text = len(text)

for i in range(length_text - 1, -1, -1):
    reversed_text += text[i]

print("Строка с зеркальным порядком слов:", mirror_text)
print("Строка в обратном порядке:", reversed_text)


text = input('Введите английский текст: ')

new_text = ''
current_word = ''

for symbol in text:
    if symbol == ' ' or symbol == ',' or symbol == '.':
        if current_word:

            length_current_word = len(current_word)

            if length_current_word > 20:

                for j in range(length_current_word):
                    if j > 0 and j % 20 == 0:
                        new_text += ' '

                    new_text += current_word[j]
            else:
                new_text += current_word
            current_word = ''

        new_text += symbol
    elif 'A' <= symbol <= 'Z' or 'a' <= symbol <= 'z':
        current_word += symbol
    else:
        new_text += symbol

if current_word:

    length_current_word = len(current_word)

    if length_current_word > 20:
        for j in range(length_current_word):
            if j > 0 and j % 20 == 0:
                new_text += ' '

            new_text += current_word[j]
    else:
        new_text += current_word

K = 0
current_word = ''

for symb in new_text:
    if symb == ' ' or symb == ',' or symb == '.':

        current_length = len(current_word)

        if current_length > K:
            K = current_length

        current_word = ''
    elif 'A' <= symb <= 'Z' or 'a' <= symb <= 'z':
        current_word += symb

capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
result_text = ''

for element in new_text:
    if element in capital_letters:
        index = capital_letters.index(element)
        new_index = (index + K) % 26
        result_text += capital_letters[new_index]
    elif element in lowercase_letters:
        index = lowercase_letters.index(element)
        new_index = (index + K) % 26
        result_text += lowercase_letters[new_index]
    else:
        result_text += element

print("Зашифрованный текст:", result_text)
print("K =", K)
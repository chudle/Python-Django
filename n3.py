import re

string = input("Введите текст: ")
string1 = re.sub(r'[^\w\s]', '', string)
# print("(DEBUG) string1: ", string1)
words = string1.split()
m_common = ''
c_common = 0
m_length = ''
c_length = 0
for word in words:
    if len(word) > c_length:
        c_length = len(word)
        m_length = word
    count = 0
    for c_word in words:
        if word == c_word:
            count += 1
    if count > c_common:
        c_common = count
        m_common = word
print("Самое частое слово:", m_common, "(", c_common, "раз )")
print("Самое длинное слово:", m_length, "(", c_length, "букв )")

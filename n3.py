import re

string = re.sub(r'[^\w\s]','', str(input()))
words = string.split()
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

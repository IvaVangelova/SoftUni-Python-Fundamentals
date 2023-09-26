word = input()
# lower_word = word.lower()   # 1.2) Type to for solving
counter = 0
searching_words = ['sand', 'water', 'fish', 'sun']

for i in searching_words:
    word.lower().count(i)  # lowering the word and counting it at the same time
    if i in word.lower():  # checking a word from list does it contains in lowered word?
        if word.lower().count(i) > 1:  # checking how many times i from list is in word
            counter += word.lower().count(i)  # adding the number of how many time the i is in word
        else:
            counter += 1
print(counter)

# 1.2) Type to for solving

# for i in searching_words:
#     if i in lower_word:
#         if lower_word.count(i) > 1:
#             counter += lower_word.count(i)
#         else:
#             counter += 1
# print(counter)

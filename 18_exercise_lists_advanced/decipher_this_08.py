message = input().split()
new_word = ''
for word in message:
    character_list = [index for index in word if not index.isnumeric()]
    number_list = [index for index in word if index.isnumeric()]
    character_list[0], character_list[-1] = character_list[-1], character_list[0]
    character_number = chr(int(''.join(number_list)))
    character_list.insert(0, character_number)
    new_word = ''.join(character_list)
    print(new_word, end=" ")

name_1 = input()
name_2 = input()
save = name_1
for i in range(len(name_1)):
    slice_1 = name_1[i + 1:]
    slice_2 = name_2[:i + 1]
    current_word = slice_2 + slice_1
    if current_word != save:
        print(current_word)
        save = current_word

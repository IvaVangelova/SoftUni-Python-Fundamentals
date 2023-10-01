key = int(input())
number_of_lines = int(input())
decrypting_word = ''
for i in range(number_of_lines):
    character = ord(input())
    current_sum = key + character
    decrypting_word += chr(current_sum)

print(decrypting_word)

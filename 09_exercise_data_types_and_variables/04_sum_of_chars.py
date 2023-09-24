number_of_characters = int(input())
total = 0
for i in range(number_of_characters):
    character = input()
    total += ord(character)
print(f"The sum equals: {total}")

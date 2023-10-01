list_of_integers = ([int(number) for number in input().split()])
count_numbers_removed = int(input())

for i in range(count_numbers_removed):
    list_of_integers.remove(min(list_of_integers))
list_to_strings = (str(s) for s in list_of_integers)
print(', '.join(list_to_strings))

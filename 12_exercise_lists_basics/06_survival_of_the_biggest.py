list_of_integers = ([int(number) for number in input().split()])
count_numbers_removed = int(input())
# small = max(list_of_integers)

# for i in range(count_numbers_removed):
#     for j in list_of_integers:
#         if list_of_integers[j] < small:
#             small = list_of_integers[j]
#     list_of_integers.remove(small)
# print(list_of_integers)

for i in range(count_numbers_removed):
    list_of_integers.remove(min(list_of_integers))

print(', 'list_of_integers.join())
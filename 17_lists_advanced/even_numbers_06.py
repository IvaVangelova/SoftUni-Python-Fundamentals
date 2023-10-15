# given_numbers = [int(number) for number in input().split(", ")]
# even_index_list = [given_numbers.index(i) for i in given_numbers if i % 2 == 0]
# print(even_index_list)

given_numbers = [int(number) for number in input().split(", ")]
even_index_list = [index for index, item in enumerate(given_numbers) if item % 2 == 0]
print(even_index_list)

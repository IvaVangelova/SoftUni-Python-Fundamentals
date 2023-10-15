given_numbers = input().split(", ")
even_index_list = [given_numbers.index(i) for i in given_numbers if int(i) % 2 == 0]
print(even_index_list)

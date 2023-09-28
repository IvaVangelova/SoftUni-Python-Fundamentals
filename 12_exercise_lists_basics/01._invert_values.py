numbers_to_list = list(map(int, input().split(' ')))
negative_list = []

for i in range(len(numbers_to_list)):

    negative_list.append(numbers_to_list[i]*-1)

print(negative_list)

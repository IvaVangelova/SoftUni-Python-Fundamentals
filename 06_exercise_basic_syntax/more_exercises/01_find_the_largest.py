# number = input()
# my_list = []
# for i in number:
#     my_list.append(i)
# my_list.sort(reverse=True)
# print(''.join(my_list))

my_list = list(input())
print(''.join(sorted(my_list, reverse=True)))

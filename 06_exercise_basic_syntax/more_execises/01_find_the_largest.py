number = int(input())
number_as_string = str(number)
my_list = []
for i in number_as_string:
    my_list.append(i)

my_list.sort(reverse=True)
print(''.join(my_list))


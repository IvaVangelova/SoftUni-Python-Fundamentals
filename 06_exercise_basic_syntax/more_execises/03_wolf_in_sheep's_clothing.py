my_list = input()
sheep_list = list(my_list.split())
# for i in range(len(sheep_list) - 1, -1, -1):
    # if i == e == 'wolf':
    #     print("Please go away and stop eating my sheep")
    # else:
    #     print(f'Oi! Sheep number {sheep_list[i - 1]}! You are about to be eaten by a wolf!')
    #
    # print(sheep_list[i])
if 'wolf' in sheep_list or 'wolf,' in sheep_list:

    print(sheep_list)
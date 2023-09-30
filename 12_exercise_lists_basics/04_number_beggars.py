money_list = ([int(s) for s in input().split(", ")])
count_of_beggars = int(input())
sum_received = []

for i in range(count_of_beggars):

    current_sum = 0

    for beggar in range(i, len(money_list), count_of_beggars):

        current_sum += money_list[beggar]
    sum_received.append(current_sum)

print(sum_received)

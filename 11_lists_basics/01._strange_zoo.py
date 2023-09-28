# animal_list = []
#
# for _ in range(3):
#     part = input()
#     animal_list.append(part)
# animal_list[0], animal_list[2] = animal_list[2], animal_list[0]
# print(animal_list)

tail = input()
body = input()
head = input()
total_body = [tail, body, head]
total_body[0], total_body[2] = total_body[2], total_body[0]
print(total_body)

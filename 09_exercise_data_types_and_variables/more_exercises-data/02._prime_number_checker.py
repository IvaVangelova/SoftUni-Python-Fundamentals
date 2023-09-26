number = int(input())
is_not_prime = True
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            is_not_prime = False
if is_not_prime:
    print('True')
else:
    print('False')

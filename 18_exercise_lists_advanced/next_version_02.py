""" Checking witch version is """
version_number = [int(number) for number in input().split(".")]
for i in range(1, 11):
    for j in range(1, 11):
        for k in range(1, 11):
            if k == 10:
                version_number[2] = 0
            else:
                version_number[2] += 1

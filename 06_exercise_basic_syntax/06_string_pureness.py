number = int(input())
for i in range(number):
    string = input()
    for j in string:
        if j == "," or j == "." or j == "_":
            print(f"{string} is not pure!")
            break
    else:
        print(f"{string} is pure.")

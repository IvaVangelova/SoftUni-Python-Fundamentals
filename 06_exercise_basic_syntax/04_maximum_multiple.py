divisor = int(input())
boundary = int(input())
largest = divisor
for i in range(boundary, divisor, - 1):
    if i % divisor == 0:
        largest = i
        break
print(largest)

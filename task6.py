a = b = 1

n = int(input('Введите число - '))
i = 0

while i < n - 2:
    sum = a + b
    a = b
    b = sum
    i = i + 1
print(sum)
    
n = int(input("Введите номер дня недели: "))
if n == 6 or n == 7 and 0 < n < 8:
    print("Выходной день")
elif 0 < n < 6:
    print("Будний день")
else:
    print("Введите другое число")
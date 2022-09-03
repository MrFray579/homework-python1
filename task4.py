number = int(input("Введите номер четвери: "))

if number == 1:
    print("Точка лежит в промежутке x > 0, y > 0")
elif number == 2:
    print("Точка лежит в промежутке x < 0, y > 0")
elif number == 3:
    print("Точка лежит в промежутке x < 0, y < 0")
elif number == 4:
    print("Точка лежит в промежутке x > 0, y < 0")
else:
    print("Введите число от 1 до 4")

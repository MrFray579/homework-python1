from array import array


def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    array = []
    for i in range(x):
        array.append(input(f"Введите значение {xyz[i]}: "))
    return array


def is_Predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


comparison = inputNumbers(3)

if is_Predicate(comparison):
    print(True)
else:
    print(False)

    

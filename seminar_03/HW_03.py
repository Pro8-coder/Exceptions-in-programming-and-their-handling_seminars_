"""
Реализуйте метод, принимающий в качестве аргументов два целочисленных массива,
и возвращающий новый массив, каждый элемент которого равен частному элементов
двух входящих массивов в той же ячейке. Если длины массивов не равны,
необходимо как-то оповестить пользователя. Важно: При выполнении метода
единственное исключение, которое пользователь может увидеть -
RuntimeException, т.е. ваше
"""

def divide_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        raise RuntimeError("Длины массивов не совпадают")
    result = []
    for i in range(len(arr1)):
        if arr2[i] == 0:
            raise RuntimeError("Деление на ноль")
        result.append(arr1[i] / arr2[i])
    return result


arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
try:
    result = divide_arrays(arr1, arr2)
    print(result)
except RuntimeError as e:
    print(e)

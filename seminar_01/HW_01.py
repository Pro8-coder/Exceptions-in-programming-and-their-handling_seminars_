"""
Реализуйте 3 метода, чтобы в каждом из них получить разные исключения
"""


class MyException(Exception):
    def handle_division(self):
        num = int(input("Введите число: "))
        if num == 0:
            raise ZeroDivisionError("Ошибка: деление на ноль!")
        result = 100 / num
        print(result)

    def handle_index_error(self):
        try:
            my_list = [1, 2, 3]
            print(my_list[4])
        except IndexError:
            raise IndexError("Ошибка: индекс вне диапазона!")

    def handle_key_error(self):
        try:
            my_dict = {"key1": "value1", "key2": "value2"}
            print(my_dict["key3"])
        except KeyError:
            raise KeyError("Ошибка: ключ не найден!")

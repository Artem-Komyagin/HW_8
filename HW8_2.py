# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionByNull:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def divide_by_null(x, y):
        try:
            return (x / y)
        except:
            return (f"Делить на ноль нельзя")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(10, 1))
print(DivisionByNull.divide_by_null(10, 0))
print(div.divide_by_null(100, 0))
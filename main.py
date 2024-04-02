# Задание №1

# Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# Например - отлавливаем ошибку деления на ноль.

import logging

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    logger = logging.getLogger(__name__)
    format = "{asctime:<20} - {levelname:<10} - {msg}"

    logging.basicConfig(filename="./my_log_1.log", filemode="w", encoding="utf-8", level=logging.ERROR,
                        style="{", format=format)

    def func(a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            logger.error(msg=e)

    func(100, 0)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

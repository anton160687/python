# ИТОГОВОЕ ДОМАШНЕЕ ЗАДАНИЕ:

# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
#   имя файла без расширения или название каталога
#   расширение, если это файл,
#   флаг каталога, название родительского каталога.

# В процессе сбора сохраните данные в текстовый файл используя логирование.

import os
import logging
from collections import namedtuple

# Определяем именованный кортеж для хранения информации о файле или каталоге
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def get_directory_contents(directory_path):
    # Получаем список файлов и каталогов в указанной директории
    contents = os.listdir(directory_path)
    file_infos = []

    for item in contents:
        item_path = os.path.join(directory_path, item)
        is_directory = os.path.isdir(item_path)
        name, extension = os.path.splitext(item)

        # Создаем объект FileInfo и добавляем его в список
        file_info = FileInfo(name, extension, is_directory, os.path.basename(directory_path))
        file_infos.append(file_info)

    return file_infos

if __name__ == '__main__':
    import sys

    # Получаем путь до директории из аргументов командной строки
    directory_path = sys.argv[1]

    # Настройка логирования
    logging.basicConfig(filename='directory_contents.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    # Получаем информацию о содержимом директории
    directory_contents = get_directory_contents(directory_path)

    # Выводим информацию о каждом файле или каталоге и сохраняем ее в лог-файл
    for file_info in directory_contents:
        logging.info(f"Name: {file_info.name}")
        logging.info(f"Extension: {file_info.extension}")
        logging.info(f"Is Directory: {file_info.is_directory}")
        logging.info(f"Parent Directory: {file_info.parent_directory}")
        logging.info('')

    logging.info('Directory contents saved to directory_contents.log')
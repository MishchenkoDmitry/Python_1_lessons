# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <dir_name> - меняет текущую директорию на одну из внутренних
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import re
import shutil
#print('sys.argv = ', sys.argv)

def copy_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    new_file = re.sub(r".py$", r"_copy.py", dir_name)

    try:
        shutil.copy(dir_name, new_file)
        print('копия  файла {} успешно создана под именем {}'.format(dir_name, new_file))
    except FileExistsError:
        print('не удалось скопировать файл {}'.format(dir_name))


def del_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    path_dir = os.path.join(os.getcwd(), dir_name)
    answer = input("Вы точно хотите удалить файл. Да/Нет").lower()
    if answer == "да":
        try:
            os.remove(path_dir)
            print("файл {} успешно удален".format(dir_name))
        except FileExistsError:
            print("Невозможно удалить файл {} ".format(dir_name))
    else:
        print("Опреация удаления прервана")


def change_dir():
    if not dir_name:
        print("Необходимо указать имя папки вторым параметром")
        return
    path_dir = os.path.join(os.getcwd(), dir_name)

    try:
        os.chdir(path_dir)
        print("Успешный переход в директорию {} ".format(dir_name))
    except FileExistsError:
        print("Невозможно перейти в директорию {} ".format(dir_name))


def full_path():
    dir_name = sys.argv[0]
    print(os.path.join(os.getcwd(),dir_name))


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл ")
    print("cd <dir_name> - меняет текущую директорию на одну из внутренних")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": del_file,
    "cd": change_dir,
    "ls": full_path
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")



# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

for i in range(1,9):
    dir_path = os.path.join(os.getcwd(), "dir_" + str(i))
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print("Такая папка уже существует")

#Удаление
for i in range(1,9):
    dir_path = os.path.join(os.getcwd(), "dir_" + str(i))
    try:
        os.rmdir(dir_path)
    except FileExistsError:
        print("Невозможно удалить папку")
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

my_dir = os.listdir()
for el in my_dir:
    if os.path.isdir(el):
        os.rmdir(el)



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
import sys
print(os.getcwd())
print(os.path.basename(sys.argv[0]))

my_file = os.path.basename(sys.argv[0])
copy_file = re.sub(r".py$", r"_copy.py", my_file)
shutil.copy(my_file, copy_file)

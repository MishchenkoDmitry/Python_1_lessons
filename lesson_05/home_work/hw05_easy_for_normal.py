import os

def change_dir(dir_name):
    try:
        path_dir = os.path.join(os.getcwd(), dir_name)
        os.chdir(path_dir)
        print("Успешный переход в директорию {} ".format(dir_name))
    except FileExistsError:
        print("Невозможно перейти в директорию {} ".format(dir_name))

def dir_view():
    my_dir = os.listdir()
    print(my_dir)

def dir_delete(dir_name):
    try:
        path_dir = os.path.join(os.getcwd(), dir_name)
        os.rmdir(path_dir)
        print("Папка {} успешно удалена".format(dir_name))
    except FileExistsError:
        print("Невозможно удалить папку {} ".format(dir_name))

def dir_make(dir_name):
    try:
        path_dir = os.path.join(os.getcwd(), dir_name)
        os.mkdir(path_dir)
        print("Папка {} успешно создана".format(dir_name))
    except FileExistsError:
        print("Невозможно создать папку {} ".format(dir_name))
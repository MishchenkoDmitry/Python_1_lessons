# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import hw05_easy_for_normal as f
print("Меню опреаций")
print("1. Перейти в папку")
print("2. Просмотреть содержимое текущей папки")
print("3. Удалить папку")
print("4. Создать папку")

answer = int(input("Выберите номер опреации, которую вы хотите выполнить"))

if answer == 1:
    operation_ans = input("Введите название папки, в которую хотите перейти")
    f.change_dir(operation_ans)

elif answer == 2:
    f.dir_view()

elif answer == 3:
    operation_ans = input("Введите название папки, которую хотите удалить")
    f.dir_delete(operation_ans)

elif answer == 4:
    operation_ans = input("Введите название папки, которую хотите создать")
    f.dir_make(operation_ans)
else:
    print("Вы выбрали некорректную операцию")










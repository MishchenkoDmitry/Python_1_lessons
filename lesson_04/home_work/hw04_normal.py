# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

import re
my_str = "tmMmEZUOmcq"
alphabet = "[A-Z]"
my_arr = re.split(alphabet, my_str)
new_arr = [el for el in my_arr if el != ""]
print(new_arr)

alphabet = list(map(chr, range(ord('A'), ord('Z')+1)))
for el in alphabet:
    if el in my_str:
        my_str = my_str.replace(el," ")
new_arr1 = my_str.split()
print(new_arr1)

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
import re
new_str = "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
pattern = (r"[a-z]{2}([A-Z]+)[A-Z]{2}")
my_str = re.findall(pattern, new_str)
print(my_str)
# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import os
import random

lst_g = [random.randint(0, 9) for _ in range(2500)]
lst_g = list(map(str, lst_g))
lst_g = "".join(lst_g)

#Записываем файл
path = os.path.join("","random.txt")
with open(path, "w", encoding="UTF-8") as f:
    f.write(lst_g)

#Считываем файл
with open(path, "r", encoding="UTF-8") as file:
    new_lst = file.readlines()
new_lst = "".join(new_lst)
#i - накопление повторение
#j - временная переменная, в которую записываем максимальное число повторений
#k - начало отсчета(чтобы определить начало последовательности)
#posl - временная переменная, в которой будем хранить наибольшую последовательность
i = 1
j = 1
k = 0

for digit in range(1, len(new_lst)):

    if int(new_lst[digit]) - 1 == int(new_lst[digit - 1]):#ищем последовательность
        i += 1 #нашли и накапливаем повторения
        if i == 2: #Запоминаем элемент начала повторений
            k = digit - 1
        if i > j: #начинаем записывать переменную как только количество повторений стало больше чем последняя последовательность
            posl = new_lst[k: digit + 1]
    else:
        if i > 1:
            j = i #когда повторения закончились. Максимальное количество пишем в переменную
        i = 1 #повторения кончились. Обнуляем счетчик повторений


print(posl)

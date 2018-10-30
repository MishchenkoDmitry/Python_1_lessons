# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [0, 1, 2, 3] --> [0, 1, 4, 9]

my_list = [0, 1, 2, 3]
new_list = [el ** 2 for el in my_list]
print(new_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

lst1 = ["апельсин", "мандарин", "яблоко", "слива"]
lst2 = ["груша", "киви", "апельсин", "яблоко"]

new_list = [el for el in lst1 if el in lst2]
print(new_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 2
# + Элемент неотрицательный
# + Элемент не кратен 3
my_list = [-1, 2, 4, 6, 8, 9]
new_list = [el for el in my_list if (el % 2 == 0) and (el > 0) and (el % 3 != 0)]
print(new_list)
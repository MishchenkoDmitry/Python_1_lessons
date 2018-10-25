# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

lastelemnt = 15
def formationFibbonachi(number, lastelement):
    i = 2
    while i <= lastelement:
        number.append(number[i - 1] + number[i - 2])
        i += 1
    return number

firstelement = 5
numberFibbonachi = formationFibbonachi([0, 1], lastelemnt - 1)
print(numberFibbonachi[firstelement - 1:])

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def listSort (listNumber):
    n = len(listNumber)

    for j in range(0,n-1):
        for i in range(0,n-j-1):
            if listNumber[i] < listNumber[i+1]:
                listNumber[i],listNumber[i + 1] = listNumber[i + 1], listNumber[i]

    return listNumber

print(listSort([6, 5, 3, 8, 1, 2, 9, 7, 4]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def myFilter(func,myList):
    new_list = []
    for i in myList:
        if func(i) == True:
            new_list.append(i)
    return new_list

newList = filter(len,["","not null", "10", "", "null"])
print(list(newList))
mixed = ["мак", "просо", "пшено", "мак"]
print(list(myFilter(lambda x: x == "мак", mixed)))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
import math
def len_side(A, B):
    """
    С помощью функции мы получаем длину сторону по ее координатам
    """
    AB = list(map(lambda x,y: (x-y) ** 2,A, B))
    AB = math.sqrt(sum(AB))
    return AB

a1 = [2, 2]
a2 = [4, 6]
a3 = [12,6]
a4 = [10,2]
# Решение у данной задачи 2
A1A2 = len_side(a1, a2)
A3A4 = len_side(a3, a4)
A2A3 = len_side(a2, a3)
A1A4 = len_side(a1, a4)

if A1A2 == A3A4 and A2A3 == A1A4:
    print("Точки являются вершинами параллелограмма. Способ 1")
else:
    print("Точки не являются вершинами параллелограмма")



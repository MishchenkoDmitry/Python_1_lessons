# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
def round(num, numDigit):

    num = num * (10 ** numDigit) + 0.41
    num = num // 1
    return num / (10 ** numDigit)

print(round(5.4576, 3))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def checkTicket(ticket):
    ticket = str(ticket)
    i = 0
    summ1 = 0
    summ2 = 0
    for el in ticket:
        if i < 3:
            summ1 += int(el)
        else:
            summ2 += int(el)
        i += 1

    if summ1 == summ2:
        return True


ticket = 156570

if checkTicket(ticket) == True:
    print("Ваш билет счастливый")
else:
    print("Ваш билет не счастливый")






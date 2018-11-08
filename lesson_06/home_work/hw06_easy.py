# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def length(self):
        arr_len = []
        AB = math.sqrt((self.B[0] - self.A[0]) ** 2 + (self.B[1] - self.A[1]) ** 2)
        AC = math.sqrt((self.C[0] - self.A[0]) ** 2 + (self.C[1] - self.A[1]) ** 2)
        BC = math.sqrt((self.C[0] - self.B[0]) ** 2 + (self.C[1] - self.B[1]) ** 2)

        AB = math.fabs(round(AB, 2))
        AC = math.fabs(round(AC, 2))
        BC = math.fabs(round(BC, 2))

        arr_len.append(AB)
        arr_len.append(AC)
        arr_len.append(BC)

        return arr_len

    def perimetr(self):
        arr_len = self.length()
        per = arr_len[0] + arr_len[1] + arr_len[2]
        return per

    def ploshad(self):
        arr_len = self.length()
        per = self.perimetr()
        per = per / 2
        S = math.sqrt(per * (per - int(arr_len[0])) * (per - int(arr_len[1])) * (per - int(arr_len[2])))
        return round(S, 2)

    def height(self):
        arr_len = self.length()
        S = self.ploshad()
        H = 2 * S / arr_len[1]
        return round(H, 2)

my_triangle = triangle([2,2] ,[5,8], [7,5])
arr_len = my_triangle.length()

print("Длины сторон треугольника равны: ",arr_len)
print("Площадь равна: {}, периметр павен: {}, высота равна: {}".format(my_triangle.ploshad(), my_triangle.perimetr(), my_triangle.height()))

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class trap:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def lenght(self):
        arr_len = []
        AB = math.sqrt((self.B[0] - self.A[0]) ** 2 + (self.B[1] - self.A[1]) ** 2)
        BC = math.sqrt((self.C[0] - self.B[0]) ** 2 + (self.C[1] - self.B[1]) ** 2)
        CD = math.sqrt((self.D[0] - self.C[0]) ** 2 + (self.D[1] - self.C[1]) ** 2)
        DA = math.sqrt((self.A[0] - self.D[0]) ** 2 + (self.A[1] - self.D[1]) ** 2)

        AB = math.fabs(round(AB, 2))
        BC = math.fabs(round(BC, 2))
        CD = math.fabs(round(CD, 2))
        DA = math.fabs(round(DA, 2))

        arr_len.append(AB)
        arr_len.append(BC)
        arr_len.append(CD)
        arr_len.append(DA)

        return arr_len

    def perimetr(self):
        per =sum(self.lenght())
        return round(per, 3)

    def height(self):
        a = self.lenght()[0]
        b = self.lenght()[1]
        c = self.lenght()[2]
        d = self.lenght()[3]

        #ch = ((d-b) ** 2) + a ** 2 - c ** 2
        #zn = 2 * (d - b)
        h = math.sqrt(a ** 2 - ((((d-b) ** 2) + a ** 2 - c ** 2) / (2 * (d - b))) ** 2)
        return round(h , 3)

    def ploshad(self):
        arr_len = self.lenght()
        h= self.height()
        s = h * (arr_len[1] + arr_len[3]) / 2
        return round(s, 3)

my_trap = trap([0, 0], [1, 4], [5, 4], [6, 0])

if my_trap.lenght()[0] == my_trap.lenght()[2]:
    print("Трапеция равнобедренная")
    print("Периметр равен {}".format(my_trap.perimetr()))
    print("Длины сторон равны {}".format(my_trap.lenght()))
    print("Высота равна {}".format(my_trap.height()))
    print("Площадь равна {}".format(my_trap.ploshad()))
else:
    print("Трапеция не равнобедренная")
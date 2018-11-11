# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
#Общий класс Person
class Person:
    def __init__(self, first_name, surname, last_name):
        self.firstname = first_name
        self.surname = surname
        self.lastname = last_name

    def full_name(self):
        return("{} {} {}".format(self.lastname, self.firstname, self.surname))

# Класс ученик с фио родителей
class Student(Person):
    def __init__(self, first_name, surname, last_name, mother, father):
        Person.__init__(self, first_name, surname, last_name)
        self.mother = mother
        self.father = father

    def get_parrents(self):
        return [self.mother.full_name(), self.father.full_name()]

# Класс учитель с предметом
class Teacher(Person):
    def __init__(self, first_name, surname, last_name, course):
        Person.__init__(self, first_name, surname, last_name)
        self.course = course

# Класс школьный класс
class School_class():
    def __init__(self, class_room):
        self.class_room = class_room
        self.teachers = []
        self.students = []
    def add_students(self, *args):
        for i in args:
            self.students.append(i)

    def add_teachers(self, *args):
        for i in args:
            self.teachers.append(i)


# Класс школа, в который передаем заполненые школьный классы и обрабатываем
class School():
    def __init__(self):
        self.School_class = []

    def add_SchoolClasses(self, *args):
        for i in args:
            self.School_class.append(i)

    # Получить полный список всех классов школы
    def get_allClasses(self):
        arr_classes = []
        for i in self.School_class:
            arr_classes.append(i.class_room)
        return(arr_classes)

    # Получить список всех учеников в указанном классе
    def get_allStudents(self, class_room):
        arr_allstudents = []
        for i in self.School_class:
            if i.class_room == str(class_room):
                arr_allstudents.append(i.students)
        return [el.full_name() for el in arr_allstudents[0]]

    # Узнать ФИО родителей указанного ученика
    def get_parents(self, student):
       arr_allstudents = []
       for i in self.School_class:
           arr_allstudents.append(i.students)

       return [el.get_parrents() for el in arr_allstudents[0] if el.full_name() == student]


    # Получить список всех Учителей, преподающих в указанном классе
    def get_teachers(self,class_room):
        arr_teachers = []
        for i in self.School_class:
            if i.class_room == str(class_room):
                arr_teachers.append(i.teachers)
        return [el.full_name() for el in arr_teachers[0]]

 # Получить список всех предметов указанного ученика
"""
    def get_courses(self, student):
        all_students = []
        for i in self.School_class:
            all_students.append(i)


        for i in all_students:
            for z in self.School_class:
        #classes = [x for x in self.School_class if student in [y.full_name() in x.students]]
        #return [x.subject.name for x in classes[0].teachers]
"""
mother1 = Person("И.", "В.", "Иванова")
father1 = Person("Т.", "С.", "Иванов")
mother2 = Person("И.", "В.", "Сидорова")
father2 = Person("И.", "В.", "Сидоров")
mother3 = Person("И.", "В.", "Петрова")
father3 = Person("И.", "В.", "Петров")

math_subj = Teacher("И.", "И", "Козлов", "Математика")
phys_subj = Teacher("A.", "A", "Козлов","Физика")
eng_subj = Teacher("O.", "O", "Козлов","Английский язык")

student1 = Student("Д.", "Т.", "Иванов", mother1, father1)
student2 = Student("З.", "П.", "Сидоров", mother2, father2)
student3 = Student("Е.", "С.", "Петров", mother3, father3)

class1 = School_class("9 A")
class2 = School_class("8 Б")

class1.add_teachers(math_subj, eng_subj, phys_subj)
class2.add_teachers(math_subj, eng_subj)

class1.add_students(student1, student2)
class2.add_students(student3)

school = School()
school.add_SchoolClasses(class1,class2)

print("Список всех классов школы: {}".format(school.get_allClasses()))
print("Все ученики 9 А класса: {}".format(school.get_allStudents("9 A")))
print("Родители ученика Иванов Д. Т. {}".format(school.get_parents("Иванов Д. Т.")))
print("Все учителя 9 А класса {}".format(school.get_teachers("9 A")))

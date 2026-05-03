class Student:
    def __init__(self, h=160):
        self.h = h


nikocado = Student()
avocado = Student(h=170)

print(nikocado.h)
print(avocado.h)
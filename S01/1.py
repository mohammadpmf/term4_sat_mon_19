class Student():
    def __init__(self,name,surname,age=None):  # constructor تابع سازنده
        self.name=name
        self.surname=surname
        self.age=age
    def __str__(self):
        return f"{self.name} {self.surname}"

s1 = Student('neda', 'alavi', 16)
s2 = Student('ali', 'alavi')
print(s1)
print(s2)
# print(s1.age)
# print(s2.age)
# کلاسی به اسم Car تعریف کنید.
# اسم ماشین. رنگ ماشین. سال ساخت

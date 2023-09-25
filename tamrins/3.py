from tkinter import *
class Form():
    def __init__(self, root):
        self.root = root
        self.frame = LabelFrame(self.root, text='Personal Info')
        self.l1 = Label(self.frame, text='Name: ')
        self.l2 = Label(self.frame, text='Surname: ')
        self.e1 = Entry(self.frame)
        self.e2 = Entry(self.frame)
        self.b1 = Button(self.frame, text='Save')
        self.l1.grid(row=1, column=1)
        self.l2.grid(row=2, column=1)
        self.e1.grid(row=1, column=2)
        self.e2.grid(row=2, column=2)
        self.b1.grid(row=4, column=1)
    def grid(self):
        self.frame.grid()

root = Tk()
btn=Button(root, text='Ok', bg='orange')
btn.grid(row=1, column=1)
f1 = Form(root)
f1.grid()
mainloop()
# برای تمرین بین انتری دوم و دکمه یک سطر با عنوان age
# وارد کنید. مقادیر آن یک اسپین باکس از ۱ تا ۹۹ باشد که داخل آن نتوان چیز دیگری نوشت.

from tkinter import *
class Form():
    def __init__(self, root, title='Personal Info', l1="Name: ", l2='Surname: ', l3='Age: ', bg=None, fg=None):
        self.root = root
        self.frame = LabelFrame(self.root, text=title, bg=bg, fg=fg)
        self.l1 = Label(self.frame, text=l1, bg=bg, fg=fg)
        self.l2 = Label(self.frame, text=l2, bg=bg, fg=fg)
        self.l3 = Label(self.frame, text=l3, bg=bg, fg=fg)
        self.e1 = Entry(self.frame)
        self.e2 = Entry(self.frame)
        self.age = Spinbox(self.frame, from_=1, to=99, wrap=True)
        self.b1 = Button(self.frame, text='Save', command=self.save, bg=bg, fg=fg)
        self.l1.grid(row=1, column=1)
        self.l2.grid(row=2, column=1)
        self.l3.grid(row=3, column=1)
        self.e1.grid(row=1, column=2)
        self.e2.grid(row=2, column=2)
        self.age.grid(row=3, column=2)
        self.b1.grid(row=4, column=1)
    def save(self):
        f = open(f"{self.e1.get()}.txt", 'w')
        f.write(f"{self.e1.get()}\n{self.e2.get()}\n{self.age.get()}")
        f.close()
    def grid(self, row=None, column=None):
        self.frame.grid(row=row, column=column)

root = Tk()
f1 = Form(root, bg='pink', fg='purple')
f1.grid()
mainloop()
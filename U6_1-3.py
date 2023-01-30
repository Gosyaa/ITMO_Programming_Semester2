from colorsys import TWO_THIRD
from multiprocessing.connection import answer_challenge
from os import TMP_MAX
from tkinter import *
from tkinter import messagebox
import string

window = Tk()
window.title('Окошечко')
window.geometry('240x360')

def error():
    global num1, num2, ans, num
    ans.change('')
    num.clear()
    messagebox.showerror(title='Ошибка', message='Некоректный ввод')

class Main_Field:
    def __init__(self, str=''):
        self.txt = Label(window, text = str, anchor=CENTER, background='#FFFFFF')
        self.txt.place(x=0, y=0, width=240, height=70)
    def change(self, str):
        self.txt = Label(window, text = str, anchor=CENTER, background='#FFFFFF')
        self.txt.place(x=0, y=0, width=240, height=70)

class Select_Button:
    def __init__(self):
        self.rad_cacl = Radiobutton(window, text='Калькулятор', variable=mode, value=0, anchor=W, command=lambda: replace_checks(0))
        self.rad_rect = Radiobutton(window, text='Прямоугольник', variable=mode, value=1, anchor=W, command=lambda: replace_checks(1))
        self.rad_cacl.place(x=0,y=70, width=180, height=15)
        self.rad_rect.place(x=0, y=85, width=180, height=15)
class Values:
    def __init__(self):
        self.var_1 = Entry(window, textvariable=num1, background='#FFFFFF')
        self.var_2 = Entry(window, textvariable=num2, background='#FFFFFF')
        self.var_1.place(x=0, y=120, height=25, width=50)
        self.var_2.place(x=190, y=120, height=25, width=50)
    def change(self):
        global num1
        global num2
        num1, num2 = num2, num1
        self.var_1 = Entry(window, textvariable=num1, background='#FFFFFF')
        self.var_2 = Entry(window, textvariable=num2, background='#FFFFFF')
        self.var_1.place(x=0, y=120, height=25, width=50)
        self.var_2.place(x=190, y=120, height=25, width=50)
    def clear(self):
        global num1, num2
        num1.set('')
        num2.set('')
        self.var_1 = Entry(window, textvariable=num1, background='#FFFFFF')
        self.var_2 = Entry(window, textvariable=num2, background='#FFFFFF')
        self.var_1.place(x=0, y=120, height=25, width=50)

class Check_for_Calc:
    def __init__(self):
        self.c0 = Checkbutton(window, text='+', variable=args[0], offvalue=0, onvalue=1, anchor=W)
        self.c0.place(x=0, y=150, height=15, width=60)
        self.c1 = Checkbutton(window, text='-', variable=args[1], offvalue=0, onvalue=1, anchor=W)
        self.c1.place(x=60, y=150, height=15, width=60)
        self.c2 = Checkbutton(window, text='*', variable=args[2], offvalue=0, onvalue=1, anchor=E)
        self.c2.place(x=120, y=150, height=15, width=60)
        self.c3 = Checkbutton(window, text='/', variable=args[3], offvalue=0, onvalue=1, anchor=E)
        self.c3.place(x=180, y=150, height=15, width=60)
    def exterminate(self):
        self.c0.destroy()
        self.c1.destroy()
        self.c2.destroy()
        self.c3.destroy()

class Check_for_Rec:
    def __init__(self):
        self.c0 = Checkbutton(window, text='Площадь', variable=args[0], offvalue=0, onvalue=1, anchor=W)
        self.c0.place(x=0, y=150, height=15, width=120)
        self.c1 = Checkbutton(window, text='Периметр', variable=args[1], offvalue=0, onvalue=1, anchor=E)
        self.c1.place(x=120, y=150, height=15, width=120)
    def exterminate(self):
        self.c0.destroy()
        self.c1.destroy()

def replace_checks(op=0):
    global check_field, args
    check_field.exterminate()
    for i in range(4):
        args[i] = IntVar()
        args[i].set(0)
    if op == 0:
        check_field = Check_for_Calc()
    else:
        check_field = Check_for_Rec()

def main(num1, num2):
    try:
        a = float(num1)
        b = float(num2)
    except:
        error()
        return
    q = mode.get()
    if q == 0:
        out = ''
        if args[0].get() == 1:
            sum = a + b
            if sum == int(sum):
                sum = int(sum)
            else:
                sum = round(sum, 2)
            s = 'Сумма: {}'.format(sum)
            out += (s + '\n')
        if args[1].get() == 1:
            dif = a - b
            if dif == int(dif):
                dif = int(dif)
            else:
                dif = round(dif, 2)
            s = 'Разность: {}'.format(dif)
            out += (s + '\n')
        if args[2].get() == 1:
            mult = a * b
            if mult == int(mult):
                mult = int(mult)
            else:
                mult = round(mult, 2)
            s = 'Произведение: {}'.format(mult)
            out += (s + '\n')
        if args[3].get() == 1:
            try:
                div = a / b
                if div == int(div):
                    div = int(div)
                else:
                    div = round(div, 2)
                s = 'Частное: {}'.format(div)
                out += (s + '\n')
            except:
                s = 'На 0 делить нельзя!!!!'
                out += (s + '\n')
    elif q == 1:
        out = ''
        if a <= 0 or b <= 0:
            error()
            return
        if args[0].get() == 1:
            sum = 2 * (a + b)
            if sum == int(sum):
                sum = int(sum)
            else:
                sum = round(sum, 2)
            s = 'Периметр: {}'.format(sum)
            out += (s + '\n')
        if args[1].get() == 1:
            dif = a * b
            if dif == int(dif):
                dif = int(dif)
            else:
                dif = round(dif, 2)
            s = 'Площадь: {}'.format(dif)
            out += (s + '\n')
    ans.change(out)

def clear():
    global num1, num2, ans, num
    ans.change('')
    num.clear()
    try:
        rect.destroy()
    except:
        pass
def help():
    messagebox.showinfo(title='Помощь', message='Здесь Вам могли бы помочь... \n ....но не помогут(((')

def create():
    if mode.get() == 0:
        return 
    global rect
    rect = Canvas(window, height=120, width=240, bg='#FFFFFF')
    rect.place(x=0, y=240)
    rect.create_rectangle(0, 0, int(num1.get()), int(num2.get()), fill='#000000')

mode = IntVar()
num1 = StringVar()
num2 = StringVar()
mode.set(0)
num1.set('')
num2.set('')
rad = Select_Button()
q = mode.get()
ans = Main_Field()
num = Values()
replace = Button(window, text='⇄', command= lambda: num.change())
replace.place(x=120, y=120, height=25, width=25)
args = [None for i in range(4)]
for i in range(4):
    args[i] = IntVar()
    args[i].set(0)
check_field = Check_for_Calc()
Calc = Button(window, text='Результат', anchor=CENTER, background='#FFFF00', foreground='#000000', command=lambda: main(num1.get(), num2.get()))
Calc.place(x=0, y=180, height=20, width=240)
Clear = Button(window, text='Очистить', anchor=CENTER, background='#E3242B', foreground='#000000', command=lambda: clear())
Clear.place(x=0, y=200, height=20, width=240)
Create = Button(window, text='Построить фигуру', anchor=CENTER, background='#90EE90', foreground='#000000', command=lambda: create())
Create.place(x=0, y=220, height=20, width=240)

menubar = Menu(window)
filebar = Menu(menubar)
filebar.add_command(label='Выход', command=lambda: window.destroy())
menubar.add_cascade(label='Файл', menu = filebar)
op_menu = Menu(menubar)
op_menu.add_command(label='Очистить', command=lambda: clear())
menubar.add_cascade(label='Операции', menu = op_menu)
help_menu = Menu(menubar)
help_menu.add_command(label='Справка', command=lambda: help())
menubar.add_cascade(label='Помощь', menu = help_menu)
window.config(menu=menubar)

window.mainloop()
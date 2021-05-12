from tkinter import *

root = Tk()
root.title("Mnogo gotin kalkulator")
# root.iconbitmap('calc.ico')


e = Entry(root, width=45
          , borderwidth=5, bg='black', fg='red')
e.grid(row=0, column=0, columnspan=5, padx=5, pady=5)


def button_click(number):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_multyply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


button_0 = Button(root, text='0', padx=40, pady=40, command=lambda: button_click(0), bg ='black', fg='red')
button_1 = Button(root, text='1', padx=40, pady=40, command=lambda: button_click(1), bg ='black', fg='red')
button_2 = Button(root, text='2', padx=40, pady=40, command=lambda: button_click(2), bg ='black', fg='red')
button_3 = Button(root, text='3', padx=40, pady=40, command=lambda: button_click(3), bg ='black', fg='red')
button_4 = Button(root, text='4', padx=40, pady=40, command=lambda: button_click(4), bg ='black', fg='red')
button_5 = Button(root, text='5', padx=40, pady=40, command=lambda: button_click(5), bg ='black', fg='red')
button_6 = Button(root, text='6', padx=40, pady=40, command=lambda: button_click(6), bg ='black', fg='red')
button_7 = Button(root, text='7', padx=40, pady=40, command=lambda: button_click(7), bg ='black', fg='red')
button_8 = Button(root, text='8', padx=40, pady=40, command=lambda: button_click(8), bg ='black', fg='red')
button_9 = Button(root, text='9', padx=40, pady=40, command=lambda: button_click(9), bg ='black', fg='red')

button_add = Button(root, text='+', padx=40, pady=40, command=button_add, bg ='black', fg='red')
button_equal = Button(root, text='=', padx=89, pady=40, command=button_equal, bg ='midnight blue', fg='white')
button_clear = Button(root, text='Clear', padx=80, pady=40, command=button_clear, bg ='black', fg='red')

button_subtract = Button(root, text='-', padx=40, pady=40, command=button_subtract, bg ='black', fg='red')
button_mutlyply = Button(root, text='*', padx=40, pady=40, command=button_multyply, bg ='black', fg='red')
button_divide = Button(root, text='/', padx=40, pady=40, command=button_divide, bg ='black', fg='red')

# button_koren = Button(root, text='koren', padx=19, pady=19, command=button_click, bg ='black', fg='red')
# button_wtora = Button(root, text='x^2', padx=19, pady=19, command=button_click, bg ='black', fg='red')
# button_drob = Button(root, text='1/x', padx=19, pady=19, command=button_click, bg ='black', fg='red')




# butoni na ekrana
button_0.grid(row=4, column=0)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_mutlyply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
# button_koren.grid(row=1, column=3)
# button_wtora.grid(row=2, column=3)
# button_drob.grid(row=3, column=3)


root.mainloop()

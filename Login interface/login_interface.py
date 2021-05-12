from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import os

if os.path.isfile('login.txt'):
    with open('login.txt', 'r') as f:
        login = f.read()
        login = login.split(',')
        print(login)
        log = [x for x in login if x.strip()]


class Login_System:
    def __init__(self, root):
        print("sys start22222")
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1250x700+0+0")

        # ----Снимки----
        self.bg_icon = ImageTk.PhotoImage(file="bg2.jpg")
        self.user_icon = PhotoImage(file="main_user.png")
        self.pass_icon = PhotoImage(file="pass2.png")
        self.logo_icon = PhotoImage(file="user-ico.png")

        # --------Стойности-----------
        self.uname = StringVar()
        self.pass_ = StringVar()

        bg_lbl = Label(self.root, image=self.bg_icon).pack()

        title = Label(self.root, text="Login System", font=("times new roman", 40, "bold"), bg="red", fg="black", bd=10,
                      relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        Login_Frame = Frame(self.root, bg="whitesmoke")
        Login_Frame.place(x=400, y=150)

        logolbl = Label(Login_Frame, image=self.logo_icon, bd=0).grid(row=0, columnspan=2, pady=20)

        lbluser = Label(Login_Frame, text="Име", image=self.user_icon, compound=LEFT,
                        font=("times new roman", 20, "bold")).grid(row=1, column=0, padx=20, pady=10)
        txtuser = Entry(Login_Frame, bd=5, textvariable=self.uname, relief=GROOVE, font=("", 15)).grid(row=1, column=1,
                                                                                                       padx=20)

        lblpass = Label(Login_Frame, text="Парола", image=self.pass_icon, compound=LEFT,
                        font=("times new roman", 20, "bold")).grid(row=2, column=0, padx=20, pady=10)
        txtpass = Entry(Login_Frame, bd=5, textvariable=self.pass_, relief=GROOVE, font=("", 15), show='*').grid(row=2,
                                                                                                                 column=1,
                                                                                                                 padx=20)

        btn_log = Button(Login_Frame, text="Влез", width=15, font=("times new roman", 14, "bold"), bg="red", fg="black",
                         command=self.login).grid(row=3, column=1, pady=10)

    def login(self):
        if self.uname.get() == "" or self.pass_.get() == "":
            messagebox.showerror("Грешка", "Всички полета са задължителни")
        elif self.uname.get() == "Kiril" and self.pass_.get() == "1234":
            messagebox._show("Достъп", f"Здравейте {self.uname.get()}")
            quit()
        else:
            messagebox.showerror("Грешно име или парола", "Грешно име или парола")

    def quit(self):
        self.root.destroy()



root = Tk()
obj = Login_System(root)
root.mainloop()

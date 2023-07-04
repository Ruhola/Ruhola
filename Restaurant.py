import tkinter as tk
import mysql.connector


class Client:
    def __init__(self, fname, lname, age, address, mobile):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.address = address
        self.mobile = mobile


class Food:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Beverages:
    def __init__(self, title, price):
        self.title = title
        self.price = price


def create_gui(window):
    window.title('فرم دریافت اطلاعات شخص')
    window.geometry("400x200")
    f_lable = tk.Label(window, text="نام")
    f_lable.grid(row=0, column=1)
    l_lable = tk.Label(window, text="نام خانوادگی")
    l_lable.grid(row=1, column=1)
    f_entry = tk.Entry(window)
    f_entry.grid(row=0, column=2, padx=10, pady=10)
    l_entry = tk.Entry(window)
    l_entry.grid(row=1, column=2, pady=10, padx=10)
    btn_sbt = tk.Button(window, text="ثبت نام", width=10, bg='red',
                        activebackground="green", fg="black")
    btn_sbt.grid(row=2, column=2)


# creat object:
if __name__ == "__main__":
    m1 = Client("AmirHosein", "Dezyani", 10, "گرگان", "09115418888")
    m2 = Client("Ruhola", "Dezyani", 21, "گرگان", "09115418980")

    f1 = Food("Hamberger", 800000)
    f2 = Food("Pizza", 120000)

    d1 = Beverages("آبعلی", 15000)
    d2 = Beverages("coca", 20000)
    # creat Gui
    window = tk.Tk()
    create_gui(window)
    constr = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aa123456@",
        database="restaurant"
    )

window.mainloop()

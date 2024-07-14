import tkinter as tk

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    asnwer_entry.delete(0, 'end')
    asnwer_entry.insert(0, value)
def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

window = tk.Tk()
window.title('Калькулятор')
window.geometry('400x400')
window.resizable(False, False)
button_add = tk.Button(window, text = '+', width = 3, height = 2, command=add)
button_add.place(x = 70, y = 250)      #3 метода добавления кнопок "Place", "Pack", "Grid"
button_sub = tk.Button(window, text = '-', width = 3, height = 2, command=sub)
button_sub.place(x = 150, y = 250)
button_mul = tk.Button(window, text = '*', width = 3, height = 2, command=mul)
button_mul.place(x = 230, y = 250)
button_div = tk.Button(window, text = '/', width = 3, height = 2, command=div)
button_div.place(x = 310, y = 250)
number1_entry = tk.Entry(window, width=40)
number1_entry.place(x=80, y=75)
number2_entry = tk.Entry(window, width=40)
number2_entry.place(x=80, y=150)
asnwer_entry = tk.Entry(window, width=40)
asnwer_entry.place(x=80, y=330)
window.mainloop()
number1 = tk.Label(window, text="Введите первое число:")
number1.place(x=80, y=55)
number2 = tk.Label(window, text="Введите второе число:")
number2.place(x=80, y=130)
answer = tk.Label(window, text="Результат:")
answer.place(x=80, y=310)
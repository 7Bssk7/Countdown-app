import time
from tkinter import *
from tkinter import messagebox
from datetime import date

def calculate_day():
    target_date = date(2026, 9, 28)
    today = date.today

    days_left = (target_date - today).days

    if days_left > 0:
        num_days.set(f"{days_left}")

root = Tk()

root.geometry("320x250")
root.title("My Countdown")

num_days = StringVar()


calculate_day()



numDaysEntry = Entry(root, width = 3, font=("Arial", 18, ""), textvariable=num_days)

numDaysEntry.place(x= 80, y= 20)


root.mainloop()
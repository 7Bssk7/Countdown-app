import time
from tkinter import *
from tkinter import messagebox
from datetime import date

def calculate_day():
    target_date = date(2026, 9, 28)
    today = date.today()

    days_left = (target_date - today).days

    if days_left > 1:
        num_days.set(f"{days_left} days left")
    elif days_left == 1:
        num_days.set(f"{days_left} day left")
    elif days_left == 0:
        num_days.set("This is the day!")
    else:
        root.destroy()

    root.after(60000, calculate_day)   




root = Tk()

win_width = 300
win_height = 80

screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()


x_pos = screen_width - win_width - 20
y_pos = screen_height - win_height - 50  


root.geometry(f"{win_width}x{win_height}+{x_pos}+{y_pos}") 

root.title("My Countdown")


transparent_key = "gray"

num_days = StringVar()

root.config(bg=transparent_key)
root.wm_attributes("-transparentcolor", transparent_key)


root.overrideredirect(True)


display_num = Label(
    root, 
    textvariable=num_days, 
    font=("Arial", 28, "bold"), 
    bg=transparent_key,  
    fg="white"            
)
display_num.pack(expand=True)


calculate_day()

root.mainloop()
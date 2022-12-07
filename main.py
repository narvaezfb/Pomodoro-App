from tkinter import *
from time import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# checkmark = "✔"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="25:00")
    header_label.config(text="TIMER")
    check_label.config(text=" ")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps 
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        header_label.config(text="Break", fg=RED)
        countdown_mechanism(long_break_sec)
    elif reps % 2 == 0:
        header_label.config(text="Break", fg=PINK)
        countdown_mechanism(short_break_sec)
    else:
        header_label.config(text="Work", fg=GREEN)
        countdown_mechanism(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown_mechanism(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown_mechanism, count - 1)
    else:
        start_timer()
        checkmarks = ""
        for _ in range(math.floor(reps/2)):
            checkmarks += "✔"
           
        check_label.config(text=checkmarks)
  

    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# row 0
header_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, ) )
header_label.grid(row=0, column=1)


# row 1
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file= "tomato.png") 
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# row 2 

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)


# row 3 

check_label = Label(text=" ", fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)


window.mainloop()
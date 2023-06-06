import tkinter
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text="Long break", fg=RED)
        stopwatch(long_sec)
    if reps % 2 == 0:
        timer_label.config(text="Short break", fg=PINK)
        stopwatch(short_sec)
    else:
        timer_label.config(text="work", fg=GREEN)
        stopwatch(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def stopwatch(count):
    if count >= 0:
        minute = int(count/60)
        second = count % 60
        if second < 10:
            second = f"0{second}"
        clock_text = f"{minute}:{second}"
        canvas.itemconfig(time_text, text=clock_text)
        global timer
        timer = window.after(1000, stopwatch, count - 1)
    else:
        mark = ""
        work_session = int(reps/2)
        for i in range(work_session):
            mark += "✓"
        check_mark.config(text=mark)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Tomato")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")

canvas.grid(column=1, row=1)

canvas.create_image(100, 112, image=photo)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)
start_button = tkinter.Button(text="Start", highlightbackground=YELLOW, command=start_timer)
reset_button = tkinter.Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
check_mark = tkinter.Label(text="", font=(FONT_NAME, 28), bg=YELLOW, fg=GREEN)

timer_label.grid(column=1, row=0)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
check_mark.grid(column=1, row=3)

window.mainloop()

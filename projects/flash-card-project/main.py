from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# file reading with exception handling
try:
    data = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# go to next card
def next_card():
    global current_card, flip_timer
    # stop flip timer
    window.after_cancel(flip_timer)
    # change card data
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(flash_card, image=card_front)
    # start flip timer
    flip_timer = window.after(3000, flash)


# is known
def is_known():
    # remove from dataframe
    to_learn.remove(current_card)
    # update
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/to_learn.csv", index=False)
    next_card()


# flip card to other side
def flash():
    canvas.itemconfig(flash_card, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# tk inter initialization
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# timer
flip_timer = window.after(3000, flash)
# image references
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")
# GUI
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

flash_card = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, font=("ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, font=("ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

unknown_button = Button(image=wrong, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

known_button = Button(image=right, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# initialize
next_card()
# window loop
window.mainloop()

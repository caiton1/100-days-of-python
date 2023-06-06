from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for x in range(nr_letters)]
    password_symbols = [choice(symbols) for x in range(nr_symbols)]
    password_numbers = [choice(numbers) for x in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_input.delete(0, END)
    pass_input.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }
    }

    if len(website_input.get()) == 0 or len(pass_input.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please check for empty fields")
    else:
        try:
            # read file
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            # create file
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # update data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # clear out data entries for next entry
            website_input.delete(0, END)
            pass_input.delete(0, END)


# search implementation #
def search():
    try:
        with open("data.json") as file_data:
            # grab website input
            user_input = website_input.get()
            # check for input
            if len(user_input) == 0:
                messagebox.showinfo(title="Oops!", message="Please fill website field")
            else:
                # load data into variable
                data = json.load(file_data)
                # search through dictionary
                if user_input in data:
                    email = data[user_input]['email']
                    password = data[user_input]['password']
                    messagebox.showinfo(title=website_input, message=
                                        f"Email: {email}\nPassword: {password}")
                else:
                    messagebox.showinfo(title="Error", message="File not found")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File not found")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)
# image import
canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

# labels, inputs and buttons
website_label = Label(text="Website:")
website_input = Entry(width=21)
website_input.focus()
email_label = Label(text="Email/Username:")
email_input = Entry(width=35)
email_input.insert(END, "connor.nicolai.aiton@gmail.com")
pass_label = Label(text="Password:")
pass_input = Entry(width=21)
pass_button = Button(text="Generate Password", width=10,
                     font=("Ariel", 12), padx=4, command=generate_pass)
add_button = Button(text="Add", width=33, command=save)
search_button = Button(text="Search", width=10,
                       font=("Ariel", 12), padx=4, command=search)

# placing created labels, inputs and buttons on program
website_label.grid(row=1, column=0)
website_input.grid(row=1, column=1)
search_button.grid(row=1, column=2)
email_label.grid(row=2, column=0)
email_input.grid(row=2, column=1, columnspan=2)
pass_label.grid(row=3, column=0)
pass_input.grid(row=3, column=1)
pass_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=3)

window.mainloop()

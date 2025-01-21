from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- SEARCH DETAILS ------------------------------- #


def search():
    website = website_entry.get()
    try:
        with open("Data.json", mode="r") as file:
            data = json.load(file)
            dictionary = data[website]
    except KeyError:
        messagebox.showwarning(title="Error", message="Does Not Match With Existing Data!!!")
    except FileNotFoundError:
        messagebox.showinfo(title="Error!!!", message="No Data File Found...")
    else:
        email = dictionary["email"]
        password = dictionary["password"]
        messagebox.showinfo(title=f"{website}", message=f"Email: {email} \n Password: {password}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_entry.delete(0, END)
    password_list = []
    for i in range(3):
        password_list += random.choice(letters)
    for j in range(2):
        password_list += random.choice(symbols)
    for k in range(3):
        password_list += random.choice(numbers)
    random.shuffle(password_list)
    password = ""
    for a in password_list:
        password += a

    pyperclip.copy(password)
    password_entry.insert(END, string=password)
    password_entry.grid()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def store_data():
    # Get the details..
    store_website = website_entry.get()
    store_id = email_entry.get()
    store_password = password_entry.get()
    new_data = {
        store_website: {
            "email": store_id,
            "password": store_password
        }
    }

    if len(store_website) != 0 and len(store_password) != 0:
        try:
            with open("Data.json", mode='r') as file:
                # Reading old data...
                data = json.load(file)
        except FileNotFoundError:
            with open("Data.json", mode='w') as file:
                # Saving Updated data...
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data...
            data.update(new_data)

            with open("Data.json", mode='w') as file:
                # Saving Updated data...
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            email_entry.delete(0, "end")
    else:
        messagebox.showwarning(title="Error!!!", message="Please Don't Leave Any Fields Empty!!!")


'''Note:- we are updated code, we are used JSON to store records in perfect order...'''
# with open("Data.txt", mode='a') as file:
#     file.write(f"Website:- {store_website}   ")
#     file.write(f"I'd:- {store_id}   ")
#     file.write(f"Password:- {store_password} \n")
#     website_entry.delete(0, 'end')
#     password_entry.delete(0, 'end')
#     website_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas...
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# label...
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry...
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, string="ABCD@gmail.com")
email_entry.grid()
password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)


# Buttons...
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=30, command=store_data)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=search)
search_button.grid(row=1, column=2)

window.mainloop()

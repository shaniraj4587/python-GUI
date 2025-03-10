from tkinter import *

root = Tk()
root.geometry("400x400")

# grid used to place the widgets in the table format
# row and column are used to specify the position of the widget
# sticky is used to specify the position of the widget in the cell
# sticky="nsew" means the widget will be placed at the center of the cell
# sticky="n" means the widget will be placed at the top of the cell
# sticky="s" means the widget will be placed at the bottom of the cell
# sticky="e" means the widget will be placed at the right of the cell
# sticky="w" means the widget will be placed at the left of the cell
# sticky="ne" means the widget will be placed at the top right of the cell
# sticky="nw" means the widget will be placed at the top left of the cell
# sticky="se" means the widget will be placed at the bottom right of the cell
# sticky="sw" means the widget will be placed at the bottom left of the cell
# sticky="center" means the widget will be placed at the center of the cell

user = Label(root, text="Username")
password = Label(root, text="Password")
user.grid(row=0, column=0)
password.grid(row=1, column=0)

# Variables class in tkinter
# StringVar, IntVar, DoubleVar, BooleanVar

user_value = StringVar()
password_value = StringVar()

# Entry widget is used to create the input field
# textvariable is used to link the variable to the entry widget 
# attributes of Entry widget are similar to the Label widget
# padx and pady are used to specify the padding of the widget

user_entry = Entry(root, textvariable=user_value)
password_entry = Entry(root, textvariable=password_value)
user_entry.grid(row=0, column=1, padx=10, pady=10)
password_entry.grid(row=1, column=1)

def submit():
    print("Username:", user_value.get())
    print("Password:", password_value.get())

submit_btn = Button(root, text="Submit", command=submit)
submit_btn.grid(row=2, column=1)


# padx and pady are used to specify the padding of the widget
# ipadx and ipady are used to specify the internal padding of the widget
# ipadx is used to specify the horizontal padding
# ipady is used to specify the vertical padding
# example:

# user_entry = Entry(root, textvariable=user_value)
# password_entry = Entry(root, textvariable=password_value) 
# user_entry.grid(row=0, column=1, padx=10, pady=10, ipadx=10, ipady=10)
# password_entry.grid(row=1, column=1, padx=10, pady=10, ipadx=10, ipady=10)



root.mainloop()
from tkinter import *
import tkinter.messagebox as mbx

root = Tk()
root.geometry("800x400")
root.title("Message Box")

menu = Menu(root)
root.config(menu=menu)

def show_info():
    mbx.showinfo("Information", "This is an information message")

def show_warning():
    mbx.showwarning("Warning", "This is a warning message")

def show_error():
    mbx.showerror("Error", "This is an error message")

def askquestion():
    response = mbx.askquestion("Question", "Do you want to continue?")
    if response == "yes":
        print("User wants to continue")
    else:
        print("User wants to quit")


file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=show_info)
file_menu.add_command(label="Open", command=show_warning)

edit_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=show_error)
edit_menu.add_command(label="Copy", command=askquestion)
edit_menu.add_command(label="Paste")

# attributes of the messagebox module
# showinfo: Displays an information message box
# showwarning: Displays a warning message box
# showerror: Displays an error message box
# askquestion: Displays a question message box with Yes and No buttons
# askokcancel: Displays a message box with OK and Cancel buttons
# askyesno: Displays a message box with Yes and No buttons
# askretrycancel: Displays a message box with Retry and Cancel buttons
# example of above attributes
# mbx.showinfo("Information", "This is an information message")
# mbx.showwarning("Warning", "This is a warning message")
# mbx.showerror("Error", "This is an error message")
# mbx.askquestion("Question", "Do you want to continue?")
# mbx.askokcancel("OK/Cancel", "Do you want to continue?")

# in these examples they take two arguments, the first argument is the title of the message box and the second argument is the message to be displayed in the message box
# the showinfo, showwarning, and showerror functions display a message box with an OK button
# the askquestion function displays a message box with Yes and No buttons
# the askokcancel function displays a message box with OK and Cancel buttons
# the askyesno function displays a message box with Yes and No buttons
# the askretrycancel function displays a message box with Retry and Cancel buttons
# the showinfo, showwarning, and showerror functions return None





root.mainloop()
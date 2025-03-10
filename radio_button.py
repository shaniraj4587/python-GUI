from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("Radio Button")
root.geometry("400x400")

def order():
    tmsg.showinfo("Order Received", f"We have received your order for {var.get()}. Thanks for ordering")

var = StringVar()
var.set("Radio")
Label(root, text="What would you like to have sir?", font="lucida 19 bold", justify=LEFT).pack()
radio = Radiobutton(root, text="Dosa", padx=14, variable=var, value="Dosa").pack(anchor="w")
radio = Radiobutton(root, text="Idly", padx=14, variable=var, value="Idly").pack(anchor="w")
radio = Radiobutton(root, text="Paratha", padx=14, variable=var, value="Paratha").pack(anchor="w")
radio = Radiobutton(root, text="Samosa", padx=14, variable=var, value="Samosa").pack(anchor="w")
Button(root, text="Order Now", command=order).pack()

root.mainloop()
# In this code, we have created radio buttons for different food items. We have used the Radiobutton class to create radio buttons.
# The Radiobutton class takes the following attributes:
# text : text to be displayed on the radio button
# padx : padding in x direction
# variable : variable to store the value of the selected radio button
# value : value of the radio button
# command : function to be called when the radio button is clicked
# anchor : alignment of the radio button
# justify : alignment of the text on the radio button
# font : font of the text on the radio button
# The StringVar() class is used to create a variable to store the value of the selected radio button.
# The set() method is used to set the initial value of the variable.
# The get() method is used to get the value of the variable.
# The pack() method is used to display the radio button on the screen.

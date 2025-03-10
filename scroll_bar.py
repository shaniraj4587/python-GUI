from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("Scroll Bar")
root.geometry("400x400")

# to use scrollbar, we need to use the following widgets:
# 1. Scrollbar : to create the scrollbar
# 2. Listbox/Text/Canvas : to use the scrollbar with these widgets (we can use scrollbar with other widgets too)
# 3. attach the scrollbar to the widget using the xscrollcommand and yscrollcommand attributes of the widget and the set method of the scrollbar  
# 4. set the command attribute of the scrollbar to the xview or yview method of the widget
# 5. pack the scrollbar

# creating a scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# creating a listbox
lbx = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(100):
    lbx.insert(END, f"Item {i}")
lbx.pack(fill=BOTH)
scrollbar.config(command=lbx.yview)

# creating a text widget
text = Text(root, yscrollcommand=scrollbar.set)
text.pack(fill=BOTH) # fill=BOTH is used to make the widget fill the entire window
text.insert(END, "This is some text")
text.insert(END, "This is some more text")
scrollbar.config(command=text.yview)

# attributes of scrollbar
# orient : orientation of scrollbar : VERTICAL by default (can be HORIZONTAL)
# command : method to be called when scrollbar is moved : no method by default
# takefocus : whether the scrollbar can take focus : False by default (can be True)
# bd : border width of scrollbar : 2 by default (can be changed) 
# state : state of scrollbar : NORMAL by default (can be DISABLED)

# methods of scrollbar
# get() : returns the current position of the scrollbar
# set(first, last) : sets the position of the scrollbar to first and last
# activate(index) : activates the item at index index in listbox
# bbox(index) : returns the bounding box of the item at index index in listbox

# events of scrollbar
# <Button-1> : generated when the left mouse button is clicked on the scrollbar
# <ButtonRelease-1> : generated when the left mouse button is released after clicking on the scrollbar
# <Enter> : generated when the mouse pointer enters the scrollbar
# <Leave> : generated when the mouse pointer leaves the scrollbar
# <Motion> : generated when the mouse pointer is moved over the scrollbar




root.mainloop()
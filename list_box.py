from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("List Box")
root.geometry("400x400")
i = 1
def add():
    global i
    lbx.insert(END, f"item no. {i}")
    i += 1

def delete():
    lbx.delete(ACTIVE)

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First item of the listbox")

Button(root, text="Add", command=add).pack()
Button(root, text="Delete", command=delete).pack()

root.mainloop()
# attributes of listbox
# selectmode : mode of selection of listbox items : SINGLE by default (can be BROWSE, MULTIPLE, EXTENDED)
# height : height of listbox in terms of number of items : 10 by default
# width : width of listbox in terms of number of characters : 20 by default
# listvariable : variable to store the list of items in listbox : no variable by default : can be used to change the items in listbox
# activestyle : style of active item in listbox : DOTBOX by default (can be UNDERLINE)
# bg : background color of listbox : system specific color
# bd : border width of listbox : 2 by default (can be changed)
# fg : foreground color of listbox : system specific color
# font : font of the items in listbox : system specific font
# selectbackground : background color of selected item in listbox : system specific color
# selectforeground : foreground color of selected item in listbox : system specific color
# relief : relief of listbox : FLAT by default (can be SUNKEN, RAISED, GROOVE, RIDGE)
# xscrollcommand : method to be called when horizontal scrollbar is moved : no method by default
# yscrollcommand : method to be called when vertical scrollbar is moved : no method by default
# exportselection : whether the selected item in listbox can be copied to clipboard : True by default
# state : state of listbox : NORMAL by default (can be DISABLED)
# setgrid : whether the items in listbox are aligned in grid : True by default

# methods of listbox
# curselection() : returns the index of the selected item in listbox
# delete(start, end) : deletes the items in listbox from index start to index end : if end is not given, only item at index start is deleted
# get(first, last) : returns the items in listbox from index first to index last : if last is not given, only item at index first is returned
# insert(index, *elements) : inserts the elements in listbox at index index : elements can be given as arguments or as a list : if index is END, elements are inserted at the end of listbox : if index is 0, elements are inserted at the beginning of listbox : (END by default)and other keywords are also available like BEFORE, AFTER, etc.
# size() : returns the number of items in listbox
# see(index) : scrolls the listbox such that the item at index index is visible
# xview() : returns the fraction of listbox that is visible in horizontal direction
# xview_moveto(fraction) : scrolls the listbox such that the fraction of listbox that is visible in horizontal direction is fraction
# xview_scroll(number, what) : scrolls the listbox horizontally by number units in the direction given by what : number can be positive or negative : what can be UNITS or PAGES
# yview() : returns the fraction of listbox that is visible in vertical direction
# yview_moveto(fraction) : scrolls the listbox such that the fraction of listbox that is visible in vertical direction is fraction
# yview_scroll(number, what) : scrolls the listbox vertically by number units in the direction given by what : number can be positive or negative : what can be UNITS or PAGES
# activate(index) : activates the item at index index in listbox
# bbox(index) : returns the bounding box of the item at index index in listbox

# events of listbox
# <<ListboxSelect>> : generated when an item in listbox is selected
# <Double-1> : generated when an item in listbox is double clicked
# <Button-1> : generated when an item in listbox is clicked

from tkinter import *

root = Tk()
root.geometry("400x400")


# Frame is a widget that is used to contain other widgets
# It is used to group similar widgets together
# It is used to organize the widgets in a proper manner
# It is used to provide a visual structure to the application
# attributes of Frame widget
"""
bg or background: Sets the background color of the frame.
borderwidth or bd: Sets the width of the border around the frame.
relief: Specifies the type of border to draw. Common values include FLAT, SUNKEN, RAISED, GROOVE, and RIDGE.
width: Sets the width of the frame in pixels.
height: Sets the height of the frame in pixels.
padx: Adds horizontal padding around the frame (external padding).
pady: Adds vertical padding around the frame (external padding).
cursor: Specifies the cursor to use when the mouse is over the frame (e.g., "arrow", "hand2", "pencil").
highlightbackground: Color of the highlight border when the frame has focus.
highlightcolor: Color of the highlight border when the frame does not have focus.
highlightthickness: Width of the highlight border.
container: This is not an attribute but rather a role the Frame plays, as it's designed to hold other widgets.
colormap: Specifies the colormap to be used for the frame.
takefocus: Determines whether the frame can accept keyboard focus.
visual: Specifies the visual attributes of the frame.
class_: Specifies the class name of the frame (used for binding events).
name: Specifies the name of the frame.
screen: Specifies the screen on which the frame should be created.
use: Specifies the ID of an existing window to use for the frame.
"""
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)

l1 = Label(f1, text="Hello World", font="Helvetica 16 bold", fg="red", bg="grey")
l1.pack(pady=142)

f2 = Frame(root, bg="black", borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill=X)

l2 = Label(f2, text="Hello World", font="Helvetica 16 bold", fg="red", bg="black")
l2.pack(pady=142)



root.mainloop()
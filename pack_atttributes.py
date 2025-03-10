from tkinter import *

window = Tk()
window.geometry("420x420")

label1 = Label(window, text="Label 1")
label1.pack(side=TOP, fill=X, padx=10, pady=10, ipadx=5, ipady=5, anchor=CENTER, expand=True)

label2 = Label(window, text="Label 2")
label2.pack(side=BOTTOM, fill=X, padx=10, pady=10, ipadx=5, ipady=5, anchor=CENTER, expand=True)

label3 = Label(window, text="Label 3")
label3.pack(side=LEFT, fill=Y, padx=10, pady=10, ipadx=5, ipady=5, anchor=CENTER, expand=True)

label4 = Label(window, text="Label 4")
label4.pack(side=RIGHT, fill=Y, padx=10, pady=10, ipadx=5, ipady=5, anchor=CENTER, expand=True)

label5 = Label(window, text="Label 5")
label5.pack(side=TOP, fill=BOTH, padx=10, pady=10, ipadx=5, ipady=5, anchor=CENTER, expand=True)
"""
side: Specifies which side of the parent widget the widget should be placed against. Possible values are:
TOP: Place the widget at the top.
BOTTOM: Place the widget at the bottom.
LEFT: Place the widget on the left.
RIGHT: Place the widget on the right.
fill: Determines if the widget should fill the available space in its container. Possible values are:
X: Fill horizontally.
Y: Fill vertically.
BOTH: Fill both horizontally and vertically.
NONE: Do not fill (default).
expand: If set to True, the widget expands to fill any extra space in the container.
padx: Adds horizontal padding around the widget (outside the widget).
pady: Adds vertical padding around the widget (outside the widget).
ipadx: Adds internal horizontal padding inside the widget (inside the widget).
ipady: Adds internal vertical padding inside the widget (inside the widget).
anchor: Specifies the position of the widget within its allocated space. Possible values include:
N: North (top-center).
NE: North-East (top-right).
E: East (right-center).
SE: South-East (bottom-right).
S: South (bottom-center).
SW: South-West (bottom-left).
W: West (left-center).
NW: North-West (top-left).
CENTER: Center (default).
"""
window.mainloop()
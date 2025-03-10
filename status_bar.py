from tkinter import *
import time

def upload():
    status.config(text="Uploading...")
    status.update()
    # some work (like uploading a file)
    time.sleep(2)
    status.config(text="Uploaded")

root = Tk()
root.geometry("700x400")
root.title("Status Bar")

# creating a status bar
status = Label(root, text="This is the status bar", relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

# creating a button
Button(root, text="Upload", command=upload).pack()

# attributes of status bar
# relief : border decoration of status bar : FLAT by default (can be SUNKEN, RAISED, GROOVE, RIDGE)
# anchor : position of text in status bar : CENTER by default (can be N, NE, E, SE, S, SW, W, NW)

# methods of status bar
# config() : changes the attributes of the status bar
# flash() : flashes the status bar
# forget() : removes the status bar from the window
# pack() : packs the status bar
# place() : places the status bar at a specific position
# grid() : places the status bar in a grid
# lift() : raises the status bar to the top of the stacking order
# lower() : lowers the status bar to the bottom of the stacking order
# pack_forget() : removes the status bar from the window
# place_forget() : removes the status bar from the window



root.mainloop()
from tkinter import *
# we can name anything at the place of root (window -> good practice)
root = Tk()

# GUI logic
# deside full window width 
root.geometry("500x600")
# define minimum size of windows
root.minsize(300, 200)
# define maximum size of windows
root.maxsize(800, 700)
# use for label
Label1 = Label(text="Hello good morning how are you today")
# you need to always pack this 
Label1.pack()


#this is mandatry in the last 
root.mainloop()

from tkinter import *

window = Tk()
window.geometry("900x500")
window.title("this window show images")

# to display images 
photo = PhotoImage(file="images/2.png")

# to show images we need to label it 
picture = Label(image=photo)
picture.pack()

window.mainloop()
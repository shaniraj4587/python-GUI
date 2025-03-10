from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("900x500")

# to display images 
image = Image.open("images/1.jpg")  # Change the file path and extension as needed
photo = ImageTk.PhotoImage(image)

# to show images we need to label it 
picture = Label(image=photo)
picture.pack()

# while tkinter can process only png file only so, we need to to pillow here is the step:
""" 1. run in terminal -> pip install pillow
    2. import it -> from PIL import Image, ImageTk
"""
window.mainloop()
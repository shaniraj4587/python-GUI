from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Sliders")
root.geometry("400x400")

def getdollar():
    tmsg.showinfo("Amount", f"We have credited {myslider2.get()} dollars to your account")

Label(root, text="How many dollars do you want?").pack()
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
myslider2.set(50)
myslider2.pack()

Button(root, text="Get dollars", command=getdollar).pack()
myslider = Scale(root, from_=0, to=100, orient=VERTICAL)
myslider.set(50)
myslider.pack()

# attributes of slider
# from_ : minimum value of slider : 0 by default
# to : maximum value of slider: 100 by default
# length : length of slider in pixels (for horizontal slider) : 100 by default
# command : function to be called when slider value is changed : no function by default 
# showvalue : show the value of slider on the screen : True by default
# variable : variable to store the value of slider : no variable by default
# resolution : resolution of slider value (how much the value will change when we move the slider)
# width : width of slider in pixels (for vertical slider)
# sliderlength : length of slider button in pixels (for horizontal slider)
# orient : orientation of slider : HORIZONTAL or VERTICAL
# troughcolor : color of slider trough (the area where slider moves) : system specific color
# tickinterval : distance between the ticks on the slider : 0 by default
# sliderrelief : relief of slider button : FLAT by default (can be SUNKEN, RAISED, GROOVE, RIDGE)
# bd : border width of slider : 2 by default (can be changed)
# bg : background color of slider : system specific color (can be changed) 
# fg : foreground color of slider : system specific color (can be changed)
# activebackground : background color of slider when slider is active (clicked) : system specific color
# state : state of slider : NORMAL by default (can be DISABLED)
# font : font of the value shown on the slider : system specific font
# label : label of the slider : no label by default (can be added) 







root.mainloop()
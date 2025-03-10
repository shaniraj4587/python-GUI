from tkinter import *
root = Tk()
#chek button is used to select multiple options
c1 = Checkbutton(root, text="Music")
c1.pack()
c2 = Checkbutton(root, text="Video")
c2.pack()

# attribute of checkbutton
# 1. activebackground : color of the checkbutton when it is active
# 2. activeforeground : color of the text when the checkbutton is active
# 3. bg : background color of the checkbutton
# 4. bd : border width of the checkbutton
# 5. command : function to be called when the checkbutton is clicked
# 6. cursor : cursor to be displayed when the mouse is over the checkbutton
# 7. font : font of the text
# 8. fg : foreground color of the text
# 9. height : height of the checkbutton
# 10. image : image to be displayed on the checkbutton
# 11. indicatoron : 0 if the indicator is not displayed
# 12. offvalue : value to be returned when the checkbutton is not selected
# 13. onvalue : value to be returned when the checkbutton is selected
# 14. selectcolor : color of the checkbutton when it is selected
# 15. selectimage : image to be displayed when the checkbutton is selected
# 16. state : state of the checkbutton (NORMAL, ACTIVE, DISABLED)
# 17. text : text to be displayed on the checkbutton
# 18. textvariable : variable to be associated with the checkbutton
# 19. underline : index of the character to be underlined
# 20. variable : variable to be associated with the checkbutton
# 21. width : width of the checkbutton
# 22. wraplength : wrap length of the checkbutton
# 23. anchor : position of the text (N, NE, E, SE, S, SW, W, NW, CENTER)
# 24. justify : alignment of the text (LEFT, RIGHT, CENTER)
# 25. padx : padding in x-direction 26. pady : padding in y-direction


# examples of attributes of checkbutton:

# the config method is used to configure the widget's options. It can be used to set or update various attributes of the widget.
c1.config(activebackground="red")
c1.config(activeforeground="blue", bg="yellow", bd=5, cursor="hand2", font=("Arial", 12), fg="black", height=2, indicatoron=1, offvalue=0, onvalue=1, selectcolor="green", state=NORMAL, text="Music", underline=0, width=20, wraplength=100, anchor=W, justify=LEFT, padx=10, pady=5, relief=RAISED, overrelief=SUNKEN, compound=LEFT)



# methods of checkbutton
# 1. deselect() : deselects the checkbutton
# 2. flash() : flashes the checkbutton
# 3. invoke() : invokes the checkbutton
# 4. select() : selects the checkbutton
# 5. toggle() : toggles the checkbutton

# events of checkbutton
# 1. <Button-1> : when the left mouse button is clicked
# 2. <ButtonRelease-1> : when the left mouse button is released
# 3. <Enter> : when the mouse enters the checkbutton
# 4. <Leave> : when the mouse leaves the checkbutton
# 5. <Return> : when the return key is pressed
# 6. <Space> : when the space key is pressed
# 7. <FocusIn> : when the checkbutton gets the focus
# 8. <FocusOut> : when the checkbutton loses the focus
# 9. <Key> : when a key is pressed
# 10. <KeyPress> : when a key is pressed
# 11. <KeyRelease> : when a key is released
# 12. <Motion> : when the mouse is moved
# 13. <Configure> : when the size of the checkbutton is changed
# 14. <Destroy> : when the checkbutton is destroyed
# 15. <Map> : when the checkbutton is mapped
# 16. <Unmap> : when the checkbutton is unmapped

# examples of all methods and events of checkbutton
def show():
    print("Music: ", c1.var.get())
    print("Video: ", c2.var.get())
c1.var = IntVar()
c1.config(variable=c1.var)
c1.deselect(); c1.flash(); c1.invoke(); c1.select(); c1.toggle()
c1.var.set(1)
c1.var.set(0)

c1.config(command=show)
c2.var = IntVar()
#  the bind method is used to associate an event with a callback function (or event handler). This means that when a specific event occurs, the associated function is called.
c1.bind("<Button-1>", lambda e: print("Left mouse button clicked"))
c1.bind("<ButtonRelease-1>", lambda e: print("Left mouse button released"))
c1.bind("<Enter>", lambda e: print("Mouse entered"))
c1.bind("<Leave>", lambda e: print("Mouse left"))
c1.bind("<Return>", lambda e: print("Return key pressed"))
# c1.bind("<Space>", lambda e: print("Space key pressed"))
c1.bind("<FocusIn>", lambda e: print("Checkbutton got focus"))
c1.bind("<FocusOut>", lambda e: print("Checkbutton lost focus"))
c1.bind("<Key>", lambda e: print("Key pressed"))
c1.bind("<KeyPress>", lambda e: print("Key pressed"))
c1.bind("<KeyRelease>", lambda e: print("Key released"))
c1.bind("<Motion>", lambda e: print("Mouse moved"))
c1.bind("<Configure>", lambda e: print("Checkbutton size changed"))
c1.bind("<Destroy>", lambda e: print("Checkbutton destroyed"))
c1.bind("<Map>", lambda e: print("Checkbutton mapped"))
c1.bind("<Unmap>", lambda e: print("Checkbutton unmapped"))




root.mainloop()
from tkinter import *
root = Tk()
root.geometry("800x400")
root.title("event handling")

button = Button(root, text="Click me")
button.pack()

def click(event):
    print("Button clicked")

def on_click(event):
    print("Button clicked on the coordinates", event.x, event.y)

b2 = Button(root, text="Click me too")
b2.pack()
b2.bind("<Button-1>", on_click)
b2.bind("<Double-1>",quit)

button.bind("<Button-1>", click)
button.bind("<Button-3>", lambda e: print("Right button clicked"))
button.bind("<Enter>", lambda e: print("Mouse entered, event:", e))
button.bind("<Leave>", lambda e: print("Mouse left"))
button.bind("<Return>", lambda e: print("Return key pressed"))
button.bind("<Key>", lambda e: print("Key pressed" if e.char == 'z' else ""))
button.bind("<KeyPress>", lambda e: print("Key pressed"))
button.bind("<KeyRelease>", lambda e: print("Key released"))
button.bind("<Motion>", lambda e: print("Mouse moved"))
button.bind("<Configure>", lambda e: print("Button size changed"))
button.bind("<Destroy>", lambda e: print("Button destroyed"))
button.bind("<Map>", lambda e: print("Button mapped"))
button.bind("<Unmap>", lambda e: print("Button unmapped"))




root.mainloop()
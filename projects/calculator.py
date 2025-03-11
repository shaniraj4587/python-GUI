from tkinter import *

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(inptext.get()))
            inptext.set(result)
        except Exception as e:
            inptext.set("ERROR")

    elif text == "C":
        inptext.set("")

    else:
        inptext.set(inptext.get() + text)



window = Tk()
window.title("This is the calculator by shani raj")
window.geometry("400x600")
window.wm_iconbitmap("icon.ico")

inptext = StringVar()
entry = Entry(window, textvar=inptext,bd=10, font="lucida 20 bold", insertwidth=4, width=22, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4,  padx=10)

button = ["1","2", "3", "4", "5", "6", "7", "8", "9", "0","C", "/","*","-","+","="]

row = 1
col = 0
for item in button:
    b = Button(window, text=item, font="lucida 20 bold", padx=20, pady=20)
    b.grid(row=row, column=col, sticky="nsew", padx=10)
    b.bind("<Button-1>", click)
    col +=1
    if col > 2:
        col = 0
        row += 1

window.mainloop()
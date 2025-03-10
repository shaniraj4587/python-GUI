from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x400")
        self.title("GUI using classes and objects")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.status = Label(self, textvariable=self.var, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    def upload(self):
        print("button clicked")

    def createbutton(self, inptext, command):
        Button(self, text=inptext, command=command).pack()
    
if __name__ == "__main__": 
    root = GUI()
    root.status()
    root.createbutton("Upload", root.upload)
    root.mainloop()
    
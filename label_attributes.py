from tkinter import *

window = Tk()
window.title("Label Attributes Example")
window.geometry("600x900")

# Label attributes
"""
1. text: The text to display in the label.
2. font: The font of the text (e.g., ("Arial", 12)).
3. fg (foreground): The text color.
4. bg (background): The background color.
5. width: The width of the label in characters.
6. height: The height of the label in lines.
7. padx: Horizontal padding around the text.
8. pady: Vertical padding around the text.
9. relief: Border style (e.g., SOLID, RAISED, SUNKEN).
10. borderwidth: Border width.
11. image: To display image
12. compound: To display both image and text
"""

label = Label(window,
              text="This is a Label",
              font=("Arial", 24),
              fg="white",
              bg="black",
              width=20,
              height=3,
              padx=20,
              pady=20,
              relief=SOLID,
              borderwidth=5)
label.pack()

window.mainloop()

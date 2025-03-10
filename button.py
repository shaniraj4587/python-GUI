from tkinter import *

root = Tk()

f1 = Frame(root, bg="red", width=200, height=200)
f1.pack()

# button is used to display the text on the window
# this is an example of a button
# Create a button
btn = Button(root, text="Click me",
             bg="skyblue",  # Background color
             fg="black",  # Foreground color
             font=("Arial", 12),  # Font style
             width=10,  # Width in characters
             height=2,  # Height in lines
             padx=10,  # Horizontal padding
             pady=5,  # Vertical padding
             relief=RAISED,  # Border style
             borderwidth=2,  # Border width
             command=lambda: print("Button clicked!"),  # Function to call on click
             state=NORMAL,  # Button state (NORMAL, DISABLED, ACTIVE)
             cursor="hand2",  # Cursor style
             activebackground="lightgreen",  # Background color when active
             activeforeground="white")  # Foreground color when active
btn.pack()

def on_click():
    print("Hello shani how are you")

b2 = Button(root, text="Click me", command=on_click)
b2.pack()
# attributes of button widget
"""
text: The text displayed on the button.
font: The font of the text (e.g., ("Arial", 12)).
fg or foreground: The text color.
bg or background: The background color of the button.
width: The width of the button in characters.
height: The height of the button in text lines.
padx: Horizontal padding around the text.
pady: Vertical padding around the text.
relief: Border style (e.g., SOLID, RAISED, SUNKEN, GROOVE, RIDGE).
borderwidth or bd: Border width.
command: A function to be called when the button is clicked.
state: The state of the button (NORMAL, ACTIVE, DISABLED).
image: To display an image on the button.
compound: To display both text and image (TOP, BOTTOM, LEFT, RIGHT, CENTER).
anchor: Specifies how the text (or image) is positioned within the button if there's extra space.
cursor: The cursor style when the mouse is over the button (e.g., "arrow", "hand2").
activebackground: Background color when the button is active (pressed).
activeforeground: Foreground color when the button is active (pressed).
highlightbackground: Color of the highlight border when the button has focus.
highlightcolor: Color of the highlight border when the button does not have focus.
highlightthickness: Width of the highlight border.
underline: Makes the character at the given index underlined.
wraplength: Determines when a line is wrapped.
"""

root.mainloop()
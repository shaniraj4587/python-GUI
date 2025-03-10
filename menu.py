from tkinter import *
root = Tk()
root.geometry("800x400")
root.title("Menus and submenus")

# Menu are created using the Menu class
menu = Menu(root)
# attach the menu to the root window
root.config(menu=menu)

# Menu items are created using the add_cascade method
file_menu = Menu(menu, tearoff=0) # tearoff=0 removes the dashed line
menu.add_cascade(label="File", menu=file_menu)

# Menu items are created using the add_cascade method
file_menu.add_cascade(label="New", command=lambda: print("New file created"))
file_menu.add_cascade(label="Open")
file_menu.add_separator() # Adds a separator use to add a line between menu items
file_menu.add_cascade(label="Save")
file_menu.add_cascade(label="Save as")
file_menu.add_cascade(label="Close", command=lambda: print("File closed"))

# Submenus are created by creating a new Menu object and adding it to the parent menu
exit_menu = Menu(file_menu, tearoff=0) # tearoff=0 removes the dashed line
file_menu.add_cascade(label="Exit", menu=exit_menu)
exit_menu.add_cascade(label="Yes", command=root.quit)
exit_menu.add_cascade(label="No")


menu.add_cascade(label="Edit")
menu.add_cascade(label="View")
menu.add_cascade(label="Help", command=lambda: print("Help clicked"))
menu.add_cascade(label="Settings")


# Menu items can also be added using the add_command method
# The command argument is used to specify the function to be called when the menu item is clicked
# The label argument is used to specify the text to be displayed on the menu item
menu.add_command(label="About", command=lambda: print("About clicked"))
menu.add_command(label="Exit", command=quit)

# attirbutes of the Menu class
# activebackground: The background color of the menu item when the mouse is over it
# activeborderwidth: The width of the border around the menu item when the mouse is over it
# activeforeground: The foreground color of the menu item when the mouse is over it
# background: The background color of the menu item
# bd: The width of the border around the menu item
# bitmap: The bitmap to display on the menu item
# columnbreak: If set to 1, the menu item will be displayed in a new column
# command: The function to be called when the menu item is clicked
# compound: The position of the image relative to the text
# font: The font of the text on the menu item
# foreground: The foreground color of the menu item
# image: The image to display on the menu item
# label: The text to be displayed on the menu item
# menu: The submenu to display when the menu item is clicked
# state: The state of the menu item (NORMAL, DISABLED, or ACTIVE)
# underline: The index of the character to underline in the menu item
# variable: The variable to associate with the menu item
# example of above attributes
menu.add_command(label="Exit", command=quit, activebackground="red", activeforeground="blue", background="yellow", columnbreak=1, compound=LEFT, font=("Arial", 12), foreground="black", image=None, state=NORMAL, underline=0, variable=None)

# bind_all method is used to bind an event to the root window
# The first argument is the event to bind, and the second argument is the function to call when the event occurs
# The event can be a key press, a mouse click, or any other event
# The function can be a lambda function or a regular function
# The event can be specified using the following format: <modifier-type>
# The modifier can be Control, Shift, or Alt
# The type can be KeyPress, KeyRelease, ButtonPress, ButtonRelease, or any other event type
# The event can also be specified using the following format: <modifier-key>
# The key can be any key on the keyboard
# The event can also be specified using the following format: <modifier-Key-key>
# The Key can be any key on the keyboard

menu.add_cascade(label="exit", command=quit);
root.bind_all("<Control-Q>", lambda event: quit())
menu.add_cascade(label="File", menu=file_menu)
root.bind_all("<Control-F>", lambda event: print("File clicked"))
menu.add_cascade(label="Edit")
root.bind_all("<Control-e>", lambda event: print("Edit clicked"))
menu.add_cascade(label="View")
root.bind_all("<Control-v>", lambda event: print("View clicked"))

menu.add_cascade(label="Help", command=lambda: print("Help clicked")); root.bind_all("<Control-h>", lambda event: print("Help clicked"))


# methods of the Menu class
# add_cascade: Adds a submenu to the menu
# add_command: Adds a menu item to the menu
# add_separator: Adds a separator to the menu
# delete: Deletes a menu item or submenu
# entryconfig: Configures a menu item or submenu
# index: Returns the index of a menu item or submenu
# insert_cascade: Inserts a submenu at a specific index
# insert_command: Inserts a menu item at a specific index
# insert_separator: Inserts a separator at a specific index
# invoke: Invokes the menu item
# post: Displays the menu at the specified coordinates
# type: Returns the type of the menu
# unpost: Hides the menu
# xposition: Returns the x-coordinate of the menu
# yposition: Returns the y-coordinate

# examples of all above methods of the Menu class in single line
# menu.add_cascade(label="File", menu=file_menu)
# menu.add_command(label="About", command=lambda: print("About clicked"))
# menu.add_command(label="Exit", command=quit)
# menu.delete(0); menu.entryconfig(0, state=NORMAL)
# menu.index("Edit")
# menu.insert_cascade(1, label="New", menu=file_menu)
# menu.insert_command(1, label="Open")
# menu.insert_separator(1)
# menu.invoke(1)
# menu.post(100, 100)
# menu.type(1)
# menu.unpost()
# menu.xposition("Edit")
# menu.yposition("Edit")






root.mainloop()

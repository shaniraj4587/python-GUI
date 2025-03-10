from tkinter import *

root = Tk()
root.title("Tips for window")
root.geometry("800x400")
# to change the icon of the window
# root.iconbitmap("path to icon file") # path to icon file should be in .ico format (icon file) 
root.iconbitmap("icon.ico")

# some extra method for the window
root.resizable(0, 0) # to make the window non resizable (0, 0) means non resizable in both x and y directions
root.maxsize(800, 400) # to set the maximum size of the window
root.minsize(400, 200) # to set the minimum size of the window
root.configure(bg="grey") # to add extra features to the window

root.winfo_name() # returns the name of the window
root.winfo_width() # returns the width of the window
root.winfo_height() # returns the height of the window
root.winfo_geometry() # returns the geometry of the window
root.winfo_x() # returns the x coordinate of the window
root.winfo_y() # returns the y coordinate of the window
root.winfo_rootx() # returns the x coordinate of the window in the screen
root.winfo_rooty() # returns the y coordinate of the window in the screen
root.winfo_screenwidth() # returns the width of the screen
root.winfo_screenheight() # returns the height of the screen

# attributes used with root.configure() method are:
root.attributes("-alpha", 0.5) # to change the transparency of the window
root.attributes("-topmost", 1) # to bring the window to the top
root.attributes("-fullscreen", 1) # to make the window full screen

root.attributes("-toolwindow", 1) # to make the window a tool window
root.attributes("-disabled", 1) # to disable the window
root.attributes("-transparentcolor", "grey") # to make the window transparent

# all attributes in one line
# root.attributes("-alpha", 0.5, "-topmost", 1, "-fullscreen", 1, "-toolwindow", 1, "-disabled", 1, "-transparentcolor", "grey")

# methods of root
# withdraw() : removes the window from the screen without destroying it (opposite of deiconify())
# destroy() : destroys the window and removes it from the screen
# quit() : closes the window and stops the mainloop (same as destroy()) 
# deiconify() : displays the window on the screen (opposite of withdraw()) 
# iconify() : minimizes the window to the taskbar (opposite of deiconify())
# lift() : raises the window to the top of the stacking order (opposite of lower())
# lower() : lowers the window to the bottom of the stacking order (opposite of lift())
# state() : returns the state of the window (normal, iconified, withdrawn)

# events of root
# <Configure> : generated when the window is resized
# <Destroy> : generated when the window is destroyed
# <FocusIn> : generated when the window gains focus
# <FocusOut> : generated when the window loses focus
# <Map> : generated when the window is mapped
# <Unmap> : generated when the window is unmapped
# <Visibility> : generated when the window is visible

# examples of above methods in one line
# root.withdraw(), root.destroy(), root.quit(), root.deiconify(), root.iconify(), root.lift(), root.lower(), root.state()

# examples of above events in one line
# root.bind("<Configure>", lambda e: print("Window resized")), root.bind("<Destroy>", lambda e: print("Window destroyed")), root.bind("<FocusIn>", lambda e: print("Window gained focus")), root.bind("<FocusOut>", lambda e: print("Window lost focus")), root.bind("<Map>", lambda e: print("Window mapped")), root.bind("<Unmap>", lambda e: print("Window unmapped")), root.bind("<Visibility>", lambda e: print("Window visible"))





root.mainloop()
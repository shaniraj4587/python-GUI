from tkinter import *

root = Tk()
# canvas is used to draw shapes
# canvas is a rectangular area intended for drawing pictures or other complex layouts.
# canvas is used to draw shapes such as lines, rectangles, ovals, and polygons.
# canvas is a rectangular area intended for drawing pictures or other complex layouts.
# canvas is used to draw shapes such as lines, rectangles, ovals, and polygons.
# canvas is a rectangular area intended for drawing pictures or other complex layouts.

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Canvas")

can = Canvas(root, width=canvas_width, height=canvas_height)
can.pack()

# create_line() method is used to draw a line on the canvas.
# create_line(x1, y1, x2, y2, options)
# x1, y1 : coordinates of the starting point of the line
# x2, y2 : coordinates of the ending point of the line
# options : options to be used to draw the line
# fill : color to fill the line
# width : width of the line
# dash : dash pattern of the line
# arrow : arrow style of the line
# arrowshape : shape of the arrow
# smooth : smoothness of the line
# splinesteps : steps in the spline
# capstyle : style of the line cap
# joinstyle : style of the line join
# arrowfirst : arrow at the start of the line
# arrowlast : arrow at the end of the line
can.create_line(0, 0, 800, 400, fill="red", width=5)
can.create_line(0, 400, 800, 0, fill="blue", width=5)

# create_rectangle() method is used to draw a rectangle on the canvas.
# create_rectangle(x1, y1, x2, y2, options)
# x1, y1 : coordinates of the top-left corner of the rectangle
# x2, y2 : coordinates of the bottom-right corner of the rectangle
# options : options to be used to draw the rectangle
# fill : color to fill the rectangle
# outline : color of the outline of the rectangle
# width : width of the outline
# dash : dash pattern of the outline(5, 5) : 5 pixels of line, 5 pixels of space
# stipple : stipple pattern of the outline
# activefill : color to fill the rectangle when it is active
# stipple : stipple pattern of the outline
# tags : tags to be associated with the rectangle
# joinstyle : style of the rectangle join
# capstyle : style of the rectangle cap
can.create_rectangle(100, 100, 700, 300, fill="yellow", outline="green", width=5)
can.create_rectangle(200, 200, 600, 400, fill="orange", outline="purple", width=5)

# create_oval() method is used to draw an oval on the canvas.
# create_oval(x1, y1, x2, y2, options)
# x1, y1 : coordinates of the top-left corner of the bounding box of the oval
# x2, y2 : coordinates of the bottom-right corner of the bounding box of the oval
# options : options to be used to draw the oval

can.create_oval(100, 100, 700, 300, fill="yellow", outline="green", width=5, dash=(5, 5))
can.create_oval(200, 200, 600, 400, fill="orange", outline="purple", width=5, dash=(5, 5))

# create_polygon() method is used to draw a polygon on the canvas.
# create_polygon(x1, y1, x2, y2, x3, y3, ..., options)
# create_text() method is used to draw text on the canvas.
# create_text(x, y, text, options)
# create_bitmap() method is used to draw a bitmap on the canvas.
# create_bitmap(x, y, bitmap, options)
# create_window() method is used to draw a window on the canvas.
# create_window(x, y, window, options)
# create_image() method is used to draw an image on the canvas.
# create_image(x, y, image, options)
# create_arc() method is used to draw an arc on the canvas.
# create_arc(x1, y1, x2, y2, options)

# example of above methods
can.create_polygon(100, 100, 700, 300, 400, 400, fill="blue", outline="green", width=5, dash=(5, 5))
can.create_text(400, 200, text="Canvas", font=("Arial", 20))
can.create_bitmap(400, 200, bitmap="error")
can.create_window(400, 200, window=Button(root, text="Button"))
can.create_image(400, 200, image=PhotoImage(file="image.png"))
can.create_arc(100, 100, 700, 300, start=0, extent=180, fill="yellow", outline="green", width=5)




root.mainloop()
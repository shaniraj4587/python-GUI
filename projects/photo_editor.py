import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk, ImageEnhance, ImageFilter, ImageOps
import os

class PhotoEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Photo Editor")
        self.root.state('zoomed')
        
        # Variables
        self.original_image = None
        self.edited_image = None
        self.undo_stack = []
        self.redo_stack = []
        
        self.setup_ui()
        self.create_menus()

    def setup_ui(self):
        # Main container
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Toolbar
        self.create_toolbar()
        
        # Image display
        self.canvas = tk.Canvas(self.main_frame, bg='#2d2d2d')
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Sidebar with adjustments
        self.create_sidebar()

    def create_toolbar(self):
        toolbar = ttk.Frame(self.main_frame)
        toolbar.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(toolbar, text="Open", command=self.open_image).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Save", command=self.save_image).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Undo", command=self.undo).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="Redo", command=self.redo).pack(side=tk.LEFT, padx=2)

    def create_sidebar(self):
        sidebar = ttk.Frame(self.main_frame)
        sidebar.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)
        
        # Adjustment sliders
        self.create_slider(sidebar, "Brightness", 0, 2, 1, self.adjust_brightness)
        self.create_slider(sidebar, "Contrast", 0, 2, 1, self.adjust_contrast)
        self.create_slider(sidebar, "Saturation", 0, 2, 1, self.adjust_saturation)
        self.create_slider(sidebar, "Sharpness", 0, 2, 1, self.adjust_sharpness)
        
        # Filter buttons
        ttk.Label(sidebar, text="Filters").pack(pady=5)
        filters_frame = ttk.Frame(sidebar)
        filters_frame.pack()
        
        filters = [
            ("B&W", self.black_and_white),
            ("Blur", self.blur),
            ("Sharpen", self.sharpen),
            ("Emboss", self.emboss),
            ("Sepia", self.sepia),
            ("Negative", self.negative)
        ]
        
        for text, command in filters:
            ttk.Button(filters_frame, text=text, command=command).pack(pady=2)

    def create_menus(self):
        menubar = tk.Menu(self.root)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_command(label="Save", command=self.save_image)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.undo)
        edit_menu.add_command(label="Redo", command=self.redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Rotate Left", command=lambda: self.rotate(90))
        edit_menu.add_command(label="Rotate Right", command=lambda: self.rotate(-90))
        edit_menu.add_command(label="Flip Horizontal", command=self.flip_horizontal)
        edit_menu.add_command(label="Flip Vertical", command=self.flip_vertical)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        
        self.root.config(menu=menubar)

    def create_slider(self, parent, text, from_, to, default, command):
        frame = ttk.Frame(parent)
        frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(frame, text=text).pack(side=tk.LEFT)
        slider = ttk.Scale(frame, from_=from_, to=to, orient=tk.HORIZONTAL, command=command)
        slider.set(default)
        slider.pack(side=tk.LEFT, fill=tk.X, expand=True)

    def open_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.tiff")]
        )
        if file_path:
            self.original_image = Image.open(file_path)
            self.edited_image = self.original_image.copy()
            self.display_image()
            self.undo_stack.clear()
            self.redo_stack.clear()

    def save_image(self):
        if self.edited_image:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
            )
            if file_path:
                self.edited_image.save(file_path)

    def display_image(self):
        if self.edited_image:
            # Resize image to fit canvas while maintaining aspect ratio
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            ratio = min(canvas_width/self.edited_image.width, 
                       canvas_height/self.edited_image.height)
            new_size = (int(self.edited_image.width * ratio), 
                       int(self.edited_image.height * ratio))
            
            display_image = self.edited_image.copy()
            display_image.thumbnail(new_size)
            self.photo = ImageTk.PhotoImage(display_image)
            
            self.canvas.delete("all")
            self.canvas.create_image(
                canvas_width//2, canvas_height//2,
                image=self.photo, anchor="center"
            )

    # Image adjustment methods
    def adjust_brightness(self, value):
        if self.edited_image:
            self.save_state()
            enhancer = ImageEnhance.Brightness(self.edited_image)
            self.edited_image = enhancer.enhance(float(value))
            self.display_image()

    def adjust_contrast(self, value):
        if self.edited_image:
            self.save_state()
            enhancer = ImageEnhance.Contrast(self.edited_image)
            self.edited_image = enhancer.enhance(float(value))
            self.display_image()

    def adjust_saturation(self, value):
        if self.edited_image:
            self.save_state()
            enhancer = ImageEnhance.Color(self.edited_image)
            self.edited_image = enhancer.enhance(float(value))
            self.display_image()

    def adjust_sharpness(self, value):
        if self.edited_image:
            self.save_state()
            enhancer = ImageEnhance.Sharpness(self.edited_image)
            self.edited_image = enhancer.enhance(float(value))
            self.display_image()

    # Filter methods
    def black_and_white(self):
        if self.edited_image:
            self.save_state()
            self.edited_image = self.edited_image.convert('L')
            self.display_image()

    def blur(self):
        if self.edited_image:
            self.save_state()
            self.edited_image = self.edited_image.filter(ImageFilter.BLUR)
            self.display_image()

    def sharpen(self):
        if self.edited_image:
            self.save_state()
            self.edited_image = self.edited_image.filter(ImageFilter.SHARPEN)
            self.display_image()

    def emboss(self):
        if self.edited_image:
            self.save_state()
            self.edited_image = self.edited_image.filter(ImageFilter.EMBOSS)
            self.display_image()

    def sepia(self):
        if self.edited_image:
            self.save_state()
            width, height = self.edited_image.size
            pixels = self.edited_image.load()
            for x in range(width):
                for y in range(height):
                    r, g, b = self.edited_image.getpixel((x, y))[:3]
                    tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                    tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                    tb = int(0.272 * r + 0.534 * g + 0.131 * b)
                    self.edited_image.putpixel((x, y), (min(tr, 255), min(tg, 255), min(tb, 255)))
            self.display_image()

    def negative(self):
        if self.edited_image:
            self.save_state()
            if self.edited_image.mode == 'RGBA':
                # Convert to RGB if image has alpha channel
                rgb_image = self.edited_image.convert('RGB')
                self.edited_image = ImageOps.invert(rgb_image)
            else:
                self.edited_image = ImageOps.invert(self.edited_image)
            self.display_image()

    # Transform methods
    def rotate(self, angle):
        if self.edited_image:
            self.save_state()
            self.edited_image = self.edited_image.rotate(angle, expand=True)
            self.display_image()

    def flip_horizontal(self):
        if self.edited_image:
            self.save_state()
            self.edited_image = self.edited_image.transpose(Image.FLIP_LEFT_RIGHT)
            self.display_image()

    def flip_vertical(self):
        if self.edited_image:
            self.save_state()
            self.edited_image = self.edited_image.transpose(Image.FLIP_TOP_BOTTOM)
            self.display_image()

    # History management
    def save_state(self):
        if self.edited_image:
            self.undo_stack.append(self.edited_image.copy())
            self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.edited_image.copy())
            self.edited_image = self.undo_stack.pop()
            self.display_image()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.edited_image.copy())
            self.edited_image = self.redo_stack.pop()
            self.display_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoEditor(root)
    root.mainloop()
import os
from tkinter import *
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk
import math

class ImageGallery:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Image Gallery")
        self.root.state('zoomed')
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure('Sidebar.TButton', padding=10, font=('Helvetica', 10))
        
        # Colors
        self.bg_color = '#f0f0f0'
        self.sidebar_color = '#2c3e50'
        self.accent_color = '#3498db'
        
        # Configure root
        self.root.configure(bg=self.bg_color)
        
        # Create main frames
        self.setup_main_frames()
        self.setup_sidebar()
        self.setup_gallery()
        self.setup_preview()
        
        self.current_directory = None
        self.thumbnails = []
        self.current_page = 0
        self.items_per_page = 12

    def setup_main_frames(self):
        # Sidebar
        self.sidebar = Frame(self.root, bg=self.sidebar_color, width=250)
        self.sidebar.pack(side=LEFT, fill=Y)
        self.sidebar.pack_propagate(False)
        
        # Main content area
        self.main_content = Frame(self.root, bg=self.bg_color)
        self.main_content.pack(side=LEFT, fill=BOTH, expand=True)

    def setup_sidebar(self):
        # App title
        title = Label(self.sidebar, text="Image Gallery", 
                     font=('Helvetica', 16, 'bold'),
                     bg=self.sidebar_color, fg='white')
        title.pack(pady=20)
        
        # Select folder button
        select_btn = ttk.Button(self.sidebar, text="Select Folder",
                              style='Sidebar.TButton',
                              command=self.select_directory)
        select_btn.pack(pady=10, padx=20)
        
        # Path label
        self.path_label = Label(self.sidebar, 
                              text="No folder selected",
                              bg=self.sidebar_color, fg='white',
                              wraplength=220,
                              font=('Helvetica', 9))
        self.path_label.pack(pady=10, padx=20)
        
        # Navigation buttons
        self.nav_frame = Frame(self.sidebar, bg=self.sidebar_color)
        self.nav_frame.pack(pady=20)
        
        self.prev_btn = ttk.Button(self.nav_frame, text="←",
                                  command=self.prev_page, state='disabled')
        self.prev_btn.pack(side=LEFT, padx=5)
        
        self.next_btn = ttk.Button(self.nav_frame, text="→",
                                  command=self.next_page, state='disabled')
        self.next_btn.pack(side=LEFT, padx=5)

    def setup_gallery(self):
        # Gallery frame
        self.gallery_frame = Frame(self.main_content, bg=self.bg_color)
        self.gallery_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        # Grid for thumbnails
        self.thumbnail_frames = []

    def setup_preview(self):
        self.preview_window = None

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.current_directory = directory
            self.path_label.config(text=directory)
            self.current_page = 0
            self.load_images()

    def load_images(self):
        # Clear existing thumbnails
        for frame in self.thumbnail_frames:
            frame.destroy()
        self.thumbnail_frames.clear()
        self.thumbnails.clear()

        if not self.current_directory:
            return

        # Get image files
        image_files = [f for f in os.listdir(self.current_directory)
                      if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        
        # Calculate pagination
        start_idx = self.current_page * self.items_per_page
        end_idx = start_idx + self.items_per_page
        page_files = image_files[start_idx:end_idx]
        
        # Update navigation buttons
        self.prev_btn.config(state='normal' if self.current_page > 0 else 'disabled')
        self.next_btn.config(state='normal' if end_idx < len(image_files) else 'disabled')

        # Create thumbnail grid
        for idx, image_file in enumerate(page_files):
            try:
                # Create frame for thumbnail
                thumb_frame = Frame(self.gallery_frame, bg='white',
                                  relief=RAISED, borderwidth=1)
                thumb_frame.grid(row=idx//4, column=idx%4, padx=10, pady=10)
                
                # Load and resize image
                image_path = os.path.join(self.current_directory, image_file)
                img = Image.open(image_path)
                img.thumbnail((200, 200))
                photo = ImageTk.PhotoImage(img)
                
                # Create image label
                img_label = Label(thumb_frame, image=photo, bg='white')
                img_label.image = photo
                img_label.pack(padx=5, pady=5)
                
                # Create filename label
                name = image_file[:20] + '...' if len(image_file) > 20 else image_file
                name_label = Label(thumb_frame, text=name,
                                 bg='white', font=('Helvetica', 9))
                name_label.pack(pady=(0, 5))
                
                # Bind click event
                img_label.bind('<Button-1>', 
                             lambda e, path=image_path: self.show_preview(path))
                
                self.thumbnail_frames.append(thumb_frame)
                self.thumbnails.append(photo)
                
            except Exception as e:
                messagebox.showerror("Error", f"Error loading {image_file}: {str(e)}")

    def show_preview(self, image_path):
        try:
            if self.preview_window:
                self.preview_window.destroy()
            
            self.preview_window = Toplevel(self.root)
            self.preview_window.title("Image Preview")
            self.preview_window.geometry("800x600")
            
            img = Image.open(image_path)
            # Calculate scaling to fit window while maintaining aspect ratio
            display_size = (780, 580)
            img.thumbnail(display_size, Image.Resampling.LANCZOS)
            
            photo = ImageTk.PhotoImage(img)
            label = Label(self.preview_window, image=photo)
            label.image = photo
            label.pack(expand=True, fill=BOTH, padx=10, pady=10)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error displaying image: {str(e)}")

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.load_images()

    def next_page(self):
        self.current_page += 1
        self.load_images()

if __name__ == "__main__":
    root = Tk()
    app = ImageGallery(root)
    root.mainloop()
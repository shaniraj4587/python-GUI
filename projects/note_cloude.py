from tkinter import *
from tkinter import filedialog, messagebox, simpledialog, font, ttk
import os

class ModernNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Notepad")
        self.root.state('zoomed')  # Start maximized
        
        # Colors
        self.bg_color = '#f0f0f0'
        self.text_bg = '#ffffff'
        self.text_fg = '#2c3e50'
        
        # Current file
        self.current_file = None
        
        self.setup_ui()
        self.create_shortcuts()
        
    def setup_ui(self):
        # Style configuration
        style = ttk.Style()
        style.configure('TFrame', background=self.bg_color)
        
        # Main container
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=BOTH, expand=True, padx=10, pady=5)
        
        # Toolbar
        self.create_toolbar()
        
        # Text area with line numbers
        self.create_text_area()
        
        # Status bar
        self.create_status_bar()
        
        # Menu
        self.create_menu()

    def create_toolbar(self):
        toolbar = ttk.Frame(self.main_frame)
        toolbar.pack(fill=X, pady=(0, 5))
        
        # Toolbar buttons
        ttk.Button(toolbar, text="New", command=self.new_file).pack(side=LEFT, padx=2)
        ttk.Button(toolbar, text="Open", command=self.open_file).pack(side=LEFT, padx=2)
        ttk.Button(toolbar, text="Save", command=self.save_file).pack(side=LEFT, padx=2)
        
        ttk.Separator(toolbar, orient=VERTICAL).pack(side=LEFT, padx=5, fill=Y)
        
        # Font selection
        ttk.Label(toolbar, text="Font:").pack(side=LEFT, padx=5)
        self.font_family = ttk.Combobox(toolbar, values=list(font.families()), width=20)
        self.font_family.set("Arial")
        self.font_family.pack(side=LEFT, padx=2)
        self.font_family.bind('<<ComboboxSelected>>', self.change_font)
        
        # Font size
        ttk.Label(toolbar, text="Size:").pack(side=LEFT, padx=5)
        self.font_size = ttk.Spinbox(toolbar, from_=8, to=72, width=5)
        self.font_size.set(12)
        self.font_size.pack(side=LEFT, padx=2)
        self.font_size.bind('<Return>', self.change_font)

    def create_text_area(self):
        # Text frame with line numbers
        text_frame = ttk.Frame(self.main_frame)
        text_frame.pack(fill=BOTH, expand=True)
        
        # Line numbers
        self.line_numbers = Text(text_frame, width=4, padx=3, takefocus=0, border=0,
                               background='#f0f0f0', state='disabled')
        self.line_numbers.pack(side=LEFT, fill=Y)
        
        # Text area with scrollbars
        self.text_area = Text(text_frame, wrap=WORD, undo=True, maxundo=-1,
                            font=("Arial", 12), bg=self.text_bg, fg=self.text_fg)
        self.text_area.pack(side=LEFT, fill=BOTH, expand=True)
        
        # Scrollbars
        y_scrollbar = ttk.Scrollbar(text_frame, orient=VERTICAL, command=self.text_area.yview)
        y_scrollbar.pack(side=RIGHT, fill=Y)
        
        x_scrollbar = ttk.Scrollbar(self.main_frame, orient=HORIZONTAL, command=self.text_area.xview)
        x_scrollbar.pack(fill=X)
        
        self.text_area.config(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
        
        # Bind events
        self.text_area.bind('<Key>', self.update_line_numbers)
        self.text_area.bind('<MouseWheel>', self.update_line_numbers)

    def create_status_bar(self):
        self.status_bar = ttk.Label(self.root, text="Ready", anchor=W)
        self.status_bar.pack(fill=X, pady=2, padx=5)

    def create_shortcuts(self):
        self.root.bind('<Control-n>', lambda e: self.new_file())
        self.root.bind('<Control-o>', lambda e: self.open_file())
        self.root.bind('<Control-s>', lambda e: self.save_file())
        self.root.bind('<Control-q>', lambda e: self.quit_app())

    def update_line_numbers(self, event=None):
        lines = self.text_area.get('1.0', 'end-1c').count('\n') + 1
        line_numbers_text = '\n'.join(str(i) for i in range(1, lines + 1))
        self.line_numbers.config(state='normal')
        self.line_numbers.delete('1.0', END)
        self.line_numbers.insert('1.0', line_numbers_text)
        self.line_numbers.config(state='disabled')
        
        # Update status bar
        cursor_pos = self.text_area.index(INSERT)
        line, col = cursor_pos.split('.')
        self.status_bar.config(text=f"Line: {line} | Column: {col}")

    def new_file(self, event=None):
        self.text_area.delete(1.0, END)
        self.current_file = None
        self.status_bar.config(text="New File")

    def open_file(self, event=None):
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            self.current_file = file_path
            self.text_area.delete(1.0, END)
            with open(file_path, 'r') as file:
                self.text_area.insert(1.0, file.read())
            self.status_bar.config(text=f"Opened: {file_path}")

    def save_file(self, event=None):
        if self.current_file:
            with open(self.current_file, 'w') as file:
                file.write(self.text_area.get(1.0, END))
            self.status_bar.config(text=f"Saved: {self.current_file}")
        else:
            self.save_as()

    def save_as(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            self.current_file = file_path
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, END))
            self.status_bar.config(text=f"Saved: {file_path}")

    def quit_app(self, event=None):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.quit()

    def create_menu(self):
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)

        # File Menu
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit_app, accelerator="Ctrl+Q")

        # Edit Menu
        edit_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))

    def change_font(self, event=None):
        """Update the text area font when font selection changes"""
        try:
            font_family = self.font_family.get()
            font_size = int(self.font_size.get())
            self.text_area.configure(font=(font_family, font_size))
            self.status_bar.config(text=f"Font changed to {font_family}, size {font_size}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid font size")

if __name__ == "__main__":
    root = Tk()
    app = ModernNotepad(root)
    root.mainloop()
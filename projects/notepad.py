from tkinter import *
from tkinter import filedialog, messagebox, simpledialog, font

def new_file():
    text_area.delete(1.0, END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, END)
            text_area.insert(1.0, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, END))

def quit_app():
    root.quit()

def about():
    messagebox.showinfo("About", "Simple Notepad using Tkinter")

def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def change_font():
    font_dialog = Toplevel(root)
    font_dialog.title("Choose Font")
    # font_dialog.geometry("400x300")

    available_fonts = list(font.families())
    font_family_var = StringVar(value="Arial")
    font_size_var = IntVar(value=14)
    font_style_var = StringVar(value="normal")

    def update_font_list(*args):
        search_term = font_filter_var.get().lower()
        font_listbox.delete(0, END)
        for f in available_fonts:
            if search_term in f.lower():
                font_listbox.insert(END, f)

    Label(font_dialog, text="Font:").grid(row=0, column=0, padx=10, pady=10)
    font_filter_var = StringVar()
    font_filter_var.trace("w", update_font_list)
    font_filter_entry = Entry(font_dialog, textvariable=font_filter_var)
    font_filter_entry.grid(row=0, column=1, padx=10, pady=10)

    font_listbox = Listbox(font_dialog, listvariable=font_family_var, height=10)
    font_listbox.grid(row=1, column=1, padx=10, pady=10)
    for f in available_fonts:
        font_listbox.insert(END, f)

    font_scrollbar = Scrollbar(font_dialog, orient=VERTICAL, command=font_listbox.yview)
    font_listbox.config(yscrollcommand=font_scrollbar.set)
    font_scrollbar.grid(row=1, column=2, sticky="ns")

    Label(font_dialog, text="Size:").grid(row=2, column=0, padx=10, pady=10)
    size_spinbox = Spinbox(font_dialog, from_=8, to=72, textvariable=font_size_var)
    size_spinbox.grid(row=2, column=1, padx=10, pady=10)

    Label(font_dialog, text="Style:").grid(row=3, column=0, padx=10, pady=10)
    style_listbox = Listbox(font_dialog, listvariable=font_style_var, height=4)
    style_listbox.grid(row=3, column=1, padx=10, pady=10)
    for style in ["normal", "bold", "italic", "bold italic"]:
        style_listbox.insert(END, style)

    def apply_font():
        selected_font = font_listbox.get(ACTIVE)
        selected_size = font_size_var.get()
        selected_style = style_listbox.get(ACTIVE)
        text_area.config(font=(selected_font, selected_size, selected_style))
        font_dialog.destroy()

    Button(font_dialog, text="OK", command=apply_font).grid(row=4, column=0, columnspan=2, pady=10)

root = Tk()
root.title("Notepad")
root.geometry("800x600")

# Create a Text widget with a scrollbar
text_frame = Frame(root)
text_frame.pack(expand=True, fill=BOTH)

text_scrollbar = Scrollbar(text_frame)
text_scrollbar.pack(side=RIGHT, fill=Y)

text_area = Text(text_frame, font="Arial 14", undo=True, yscrollcommand=text_scrollbar.set)
text_area.pack(expand=True, fill=BOTH)
text_scrollbar.config(command=text_area.yview)

# Create a Menu bar
menu_bar = Menu(root)

# File menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Font menu
font_menu = Menu(menu_bar, tearoff=0)
font_menu.add_command(label="Change Font", command=change_font)
menu_bar.add_cascade(label="Font", menu=font_menu)

# Help menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Configure the menu bar
root.config(menu=menu_bar)

root.mainloop()
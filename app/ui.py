import tkinter as tk
from tkinter import Tk
from tkinter import filedialog



class FileCleanerApp:

    def __init__(self, root : Tk):
        self.root = root
        self.root.title('Decluttr')

        self.root.geometry("500x500")

        self.welcome_label = tk.Label(root, text="Welcome to Decluttr")
        self.welcome_label.pack(pady=10)

        self.initial_label = tk.Label(root, text="Please select the directory you want to clean")
        self.initial_label.pack(pady=10)

        self.browse_directory_button = tk.Button(root, text="Browse", command=self.browse_directory)
        self.browse_directory_button.pack(pady=5)

        self.selected_directory = ""

        self.directory_label = tk.Label(root, text="No directory selected")
        self.directory_label.pack(pady=10)

        self.file_types = [".pdf", ".jpg", ".txt", ".png", ".sql", ".mp4", ".zip"]
        self.check_vars = {}

        checkbox_frame = tk.Frame(root)
        checkbox_frame.pack(pady=10)

        columns = 4  # Number of columns per row
        for i, ext in enumerate(self.file_types):
            var = tk.BooleanVar()
            cb = tk.Checkbutton(checkbox_frame, text=ext, variable=var)
            cb.grid(row=i // columns, column=i % columns, padx=10, pady=5, sticky="w")
            self.check_vars[ext] = var


    
    def browse_directory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.selected_directory = directory_path
            self.directory_label.config(text="Selected: "  + self.selected_directory)










        
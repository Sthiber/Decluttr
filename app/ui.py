import tkinter as tk
import os
from tkinter import Tk
from tkinter import filedialog
from tkinter import messagebox




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

        self.file_types = [".pdf", ".jpg", ".txt", ".png", ".sql", ".mp4", ".zip", ".py"]
        self.check_vars = {}

        checkbox_frame = tk.Frame(root)
        checkbox_frame.pack(pady=10)

        columns = 4  
        for i, ext in enumerate(self.file_types):
            var = tk.BooleanVar()
            cb = tk.Checkbutton(checkbox_frame, text=ext, variable=var)
            cb.grid(row=i // columns, column=i % columns, padx=10, pady=5, sticky="w")
            self.check_vars[ext] = var
        
        self.new_folder_label = tk.Label(root, text="Enter the directory name to send selected files to:")
        self.new_folder_label.pack(pady=5)
        self.folder_name_entry = tk.Entry(root)
        self.folder_name_entry.pack(pady=5)

        self.start_button = tk.Button(root, text="Start Cleaning", command=self.start_cleaning)
        self.start_button.pack(pady=10)


    
    def browse_directory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.selected_directory = directory_path
            self.directory_label.config(text="Selected: "  + self.selected_directory)

    def start_cleaning(self):
        directory = self.selected_directory
        selected_types = [ext for ext, var in self.check_vars.items() if var.get()]
        folder_name = self.folder_name_entry.get().strip()

        if not directory:
            messagebox.showerror(title="No Selected Directory", message="No directory selected to clean")
        
        if len(selected_types) == 0:
            messagebox.showerror(title="No Selected File Types", message="Please select atleast one file type to extract!")

        if not folder_name:
            messagebox.showerror(title="No Folder Name", message="Please input the name of the folder you want to extract to")

        target_folder = os.path.join(directory, folder_name)
        os.mkdir(target_folder, exist_ok=True)
        


        
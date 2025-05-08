import tkinter as tk
import ttkbootstrap as ttk
import os
import shutil
from tkinter import Tk
from tkinter import filedialog
from tkinter import messagebox
from ttkbootstrap import Style

class FileCleanerApp:

    def __init__(self, root : Tk):
        self.root = root
        self.root.title('Decluttr')
        self.root.geometry("500x500")
        self.style = Style(theme='superhero')

        self.welcome_label = ttk.Label(root, text="Welcome to Decluttr", font=("Roboto", 36, "bold") ,bootstyle="info")
        self.welcome_label.pack(pady=10)

        self.initial_label = tk.Label(root, text="Please select the directory you want to clean", font=("Robot", 14, "bold"))
        self.initial_label.pack(pady=10)

        self.browse_directory_button = ttk.Button(root, text="Browse", command=self.browse_directory, bootstyle='info')
        self.browse_directory_button.pack(pady=5)

        self.selected_directory = ""

        self.directory_label = tk.Label(root, text="No directory selected", font=("Robot", 14, "bold"))
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
        
        self.new_folder_label = tk.Label(root, text="Enter the directory name to send selected files to:", font=("Robot", 14, "bold"))
        self.new_folder_label.pack(pady=5)
        self.folder_name_entry = tk.Entry(root)
        self.folder_name_entry.pack(pady=5)

        self.start_button = ttk.Button(root, text="Start Cleaning", command=self.start_cleaning, bootstyle='success')
        self.start_button.pack(pady=10)


    
    def browse_directory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.selected_directory = directory_path
            self.directory_label.config(text="Selected: "  + self.selected_directory, font=("Robot", 14, "bold"))

    def start_cleaning(self):
        directory = self.selected_directory
        selected_types = [ext for ext, var in self.check_vars.items() if var.get()]
        folder_name = self.folder_name_entry.get().strip()

        if not directory:
            messagebox.showerror(title="No Selected Directory", message="No directory selected to clean")
            return
        
        if len(selected_types) == 0:
            messagebox.showerror(title="No Selected File Types", message="Please select atleast one file type to extract!")
            return 

        if not folder_name:
            messagebox.showerror(title="No Folder Name", message="Please input the name of the folder you want to extract to")
            return
        
        
        summary = (f"Are you sure you want to clean this directory?\n\n"
                   f"Directory: {directory}\n"
                   f"File Types: {','.join(selected_types)}\n"
                   f"Destination Folder: {folder_name}")
        confirm = messagebox.askyesno("Confirm Cleanup", summary)

        if not confirm:
            return

        target_folder = os.path.join(directory, folder_name)

        if os.path.exists(target_folder):
            proceed = messagebox.askyesno("Folder Already Exists!", f"The folder {folder_name} already exists in the directory. \n\n Do you want to continue and move files into it?")
        
        if not proceed:
            return
        
        os.makedirs(target_folder, exist_ok=True)

        moved_count = 0

        for file in os.listdir(directory):
            full_path = os.path.join(directory, file)
            if os.path.isfile(full_path) and any(file.endswith(ext) for ext in selected_types):
                shutil.move(full_path, os.path.join(target_folder, file))
                moved_count += 1

        messagebox.showinfo("Cleaning Complete", f"Successfully moved {moved_count} file(s) to {folder_name}")
        for var in self.check_vars.values():
            var.set(False)
        
        self.folder_name_entry.delete(0, tk.END)





        
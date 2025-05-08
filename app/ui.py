import tkinter as tk
import ttkbootstrap as ttk
import os
import sys
from tkinter import Tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import PhotoImage
from ttkbootstrap import Style
from app.file_sorter import move_files_by_type

class FileCleanerApp:

    def __init__(self, root : Tk):
        self.root = root
        self.root.title('Decluttr')
        self.root.geometry("500x500")
        self.style = Style(theme='superhero')
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        icon_path = os.path.join(base_path, "assets", "decluttr.png")
        icon_image = PhotoImage(file=icon_path)
        self.root.iconphoto(True, icon_image)

        self.welcome_label = ttk.Label(root, text="Welcome to Decluttr", font=("Roboto", 36, "bold") ,bootstyle="info")
        self.welcome_label.pack(pady=10)

        self.initial_label = ttk.Label(root, text="Please select the directory you want to clean", font=("Roboto", 14), bootstyle="info")
        self.initial_label.pack(pady=10)

        self.browse_directory_button = ttk.Button(root, text="Browse", command=self.browse_directory, bootstyle='info')
        self.browse_directory_button.pack(pady=5)

        self.selected_directory = ""

        self.directory_label = ttk.Label(root, text="No directory selected", font=("Roboto", 14, "bold"), bootstyle="secondary")
        self.directory_label.pack(pady=10)

        self.file_types = [".pdf", ".jpg", ".txt", ".png", ".sql", ".mp4", ".zip", ".py"]
        self.check_vars = {}

        checkbox_frame = ttk.Labelframe(root, text="Select file types", bootstyle="info")
        checkbox_frame.pack(pady=10, padx=10)

        columns = 4  
        for i, ext in enumerate(self.file_types):
            var = ttk.BooleanVar()
            cb = ttk.Checkbutton(checkbox_frame, text=ext,variable=var, bootstyle="success")
            cb.grid(row=i // columns, column=i % columns, padx=10, pady=5, sticky="w")
            self.check_vars[ext] = var
        
        self.new_folder_label = ttk.Label(root, text="Enter the directory name to send selected files to:", font=("Roboto", 14), bootstyle="info")
        self.new_folder_label.pack(pady=10)
        self.folder_name_entry = tk.Entry(root)
        self.folder_name_entry.pack(pady=5)

        self.start_button = ttk.Button(root, text="Start Cleaning", command=self.start_cleaning, bootstyle='success')
        self.start_button.pack(pady=10)


    
    def browse_directory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.selected_directory = directory_path
            self.directory_label.config(text="Selected: "  + self.selected_directory, font=("Roboto", 14, "bold"))

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
        
        moved_count = move_files_by_type(directory, selected_types, folder_name)

        if moved_count == 0:
            try:
                os.rmdir(target_folder)
            except OSError:
                pass

            messagebox.showinfo("Done","No files matched the selected types.")
        else:
            messagebox.showinfo("Cleaning Complete", f"Successfully moved {moved_count} file(s) to {folder_name}")

        for var in self.check_vars.values():
            var.set(False)
        
        self.folder_name_entry.delete(0, tk.END)





        
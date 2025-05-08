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

        
    
    def browse_directory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.selected_directory = directory_path
            print('The selected directory is: ', directory_path)









        
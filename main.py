import tkinter as tk
from app.ui import FileCleanerApp


def main():
    root = tk.Tk()
    app = FileCleanerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
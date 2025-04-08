# This is the menu, DON'T TOUCH IT! MY FILE!
# Vincent's code
import tkinter as tk
from tkinter import ttk

from eur import EUR
from usd import USD
from gbp import GBP

# Global variable to track program state
ended = 0  # Initialize to 0 to indicate the program is running


def main():
    global ended  # Declare 'ended' as a global variable
    root = tk.Tk()  # Create the main Tkinter root window
    root.title('Main Menu')  # Set the title of the window

    # Clear any existing widgets in the root window
    for widget in root.winfo_children():
        widget.destroy()

    def eur():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window
        new_root = tk.Tk()
        EUR(new_root)  # Pass the file_path to the Chk class
        ended = 1
    def usd():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window
        new_root = tk.Tk()
        USD(new_root)  # Pass the file_path to the Chk class
        ended = 1
    def gbp():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window
        new_root = tk.Tk()
        GBP(new_root)  # Pass the file_path to the Chk class
        ended = 1

    
    def end_program():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window
        import os
        video_script_path = os.path.abspath("main_menu.py")
        os.system(f'python "{video_script_path}"')
        ended = 1
    
    # Create a main frame inside the window with padding
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    # Configure resizing behavior
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Create buttons for the main menu
    ttk.Button(mainframe, text='USD', command=usd).grid(column=1, row=2)
    ttk.Button(mainframe, text='EUR', command=eur).grid(column=1, row=3)
    ttk.Button(mainframe, text='GBP', command=gbp).grid(column=2, row=2)
    ttk.Button(mainframe, text='Close', command=end_program).grid(column=2, row=8)

    # Add a label for user instructions
    ttk.Label(mainframe, text='Please choose a function:').grid(column=2, row=1)

    # Add padding to all child widgets inside 'mainframe'
    for child in mainframe.winfo_children():
        child.grid_configure(padx=10, pady=10)

    # Start the Tkinter event loop
    root.mainloop()
    return ended


if __name__ == "__main__":
    while ended == 0:
        ended = main()  # Call the main function to run the application
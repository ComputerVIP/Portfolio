# This is the menu, DON'T TOUCH IT! MY FILE!
# Vincent's code
import os
import tkinter as tk
from tkinter import ttk


# Global variable to track program state
ended = 0  # Initialize to 0 to indicate the program is running


def main():
    global ended  # Declare 'ended' as a global variable
    root = tk.Tk()  # Create the main Tkinter root window
    root.title('Main Menu')  # Set the title of the window

    # Clear any existing widgets in the root window
    for widget in root.winfo_children():
        widget.destroy()

    def restart():
        root.destroy()  # Close the current window
        main()


    def end_program():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window
        ended = 1

    def run_battle():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window
        video_script_path = os.path.abspath("Battle_simulator/main.py")

        # Run the Python script
        os.system(f'python "{video_script_path}"')
        ended = 1
        

    def battle_desc():
        global ended  # Declare 'ended' as a global variable

        # Clear all widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Create a new frame for the video description
        desc_frame = ttk.Frame(root, padding="3 3 12 12")
        desc_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Read the content of 'video_desc.txt'
        with open('Battle_simulator/battle_desc.txt', 'r') as file:
            text = file.read()  # Read the file content as a string

        # Create a label to display the text
        ttk.Label(desc_frame, text=text, wraplength=400).grid(column=0, row=0, padx=10, pady=10)

        # Add a close button to return to the main menu
        ttk.Button(desc_frame, text="Close", command=restart).grid(column=0, row=1, pady=10)

        ended = 1

    def battle_menu():
        # Clear all widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Create a new frame for the "Goals" section
        goals_frame = ttk.Frame(root, padding="3 3 12 12")
        goals_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Add the "Check goal" and "Edit goal" buttons
        ttk.Button(goals_frame, text='Show description', command=battle_desc).grid(column=0, row=1)
        ttk.Button(goals_frame, text='Run program', command=run_battle).grid(column=1, row=1)
        ttk.Button(goals_frame, text="Back to menu", command=restart).grid(column=0, row=2, pady=10, columnspan=2)

        ttk.Label(goals_frame, text='Choose a function:').grid(column=0, row=0, columnspan=2, pady = 20, padx=20)

        # Add padding to all child widgets inside 'goals_frame'
        for child in goals_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)
    




    def run_video():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window
        video_script_path = os.path.abspath("Video_mp4/video_mp4.py")

        # Run the Python script
        os.system(f'python "{video_script_path}"')
        ended = 1
        

    def video_desc():
        global ended  # Declare 'ended' as a global variable

        # Clear all widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Create a new frame for the video description
        desc_frame = ttk.Frame(root, padding="3 3 12 12")
        desc_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Read the content of 'video_desc.txt'
        with open('Video_mp4/video_desc.txt', 'r') as file:
            text = file.read()  # Read the file content as a string

        # Create a label to display the text
        ttk.Label(desc_frame, text=text, wraplength=400).grid(column=0, row=0, padx=10, pady=10)

        # Add a close button to return to the main menu
        ttk.Button(desc_frame, text="Close", command=restart).grid(column=0, row=1, pady=10)

        ended = 1

    def video_menu():
        # Clear all widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Create a new frame for the "Goals" section
        goals_frame = ttk.Frame(root, padding="3 3 12 12")
        goals_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Add the "Check goal" and "Edit goal" buttons
        ttk.Button(goals_frame, text='Show description', command=video_desc).grid(column=0, row=1)
        ttk.Button(goals_frame, text='Run program', command=run_video).grid(column=1, row=1)
        ttk.Button(goals_frame, text="Back to menu", command=restart).grid(column=0, row=2, pady=10, columnspan=2)

        ttk.Label(goals_frame, text='Choose a function:').grid(column=0, row=0, columnspan=2, pady = 20, padx=20)

        # Add padding to all child widgets inside 'goals_frame'
        for child in goals_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)




    def run_nat():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window
        video_script_path = os.path.abspath("Nat_geo/nat_geo.py")

        # Run the Python script
        os.system(f'python "{video_script_path}"')
        ended = 1
        

    def nat_desc():
        global ended  # Declare 'ended' as a global variable

        # Clear all widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Create a new frame for the video description
        desc_frame = ttk.Frame(root, padding="3 3 12 12")
        desc_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Read the content of 'video_desc.txt'
        with open('Nat_geo/nat_desc.txt', 'r') as file:
            text = file.read()  # Read the file content as a string

        # Create a label to display the text
        ttk.Label(desc_frame, text=text, wraplength=400).grid(column=0, row=0, padx=10, pady=10)

        # Add a close button to return to the main menu
        ttk.Button(desc_frame, text="Close", command=restart).grid(column=0, row=1, pady=10)

        ended = 1

    def nat_menu():
        # Clear all widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Create a new frame for the "Goals" section
        goals_frame = ttk.Frame(root, padding="3 3 12 12")
        goals_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Add the "Check goal" and "Edit goal" buttons
        ttk.Button(goals_frame, text='Show description', command=nat_desc).grid(column=0, row=1)
        ttk.Button(goals_frame, text='Run program', command=run_nat).grid(column=1, row=1)
        ttk.Button(goals_frame, text="Back to menu", command=restart).grid(column=0, row=2, pady=10, columnspan=2)

        ttk.Label(goals_frame, text='Choose a function:').grid(column=0, row=0, columnspan=2, pady = 20, padx=20)

        # Add padding to all child widgets inside 'goals_frame'
        for child in goals_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    
    def run_coin():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window
        video_script_path = os.path.abspath("Coin_change/main_coin.py")

        # Run the Python script
        os.system(f'python "{video_script_path}"')
        ended = 1
        

    def coin_desc():
        global ended  # Declare 'ended' as a global variable

        # Clear all widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Create a new frame for the video description
        desc_frame = ttk.Frame(root, padding="3 3 12 12")
        desc_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Read the content of 'video_desc.txt'
        with open('Coin_change/coin_change_desc.txt', 'r') as file:
            text = file.read()  # Read the file content as a string

        # Create a label to display the text
        ttk.Label(desc_frame, text=text, wraplength=400).grid(column=0, row=0, padx=10, pady=10)

        # Add a close button to return to the main menu
        ttk.Button(desc_frame, text="Close", command=restart).grid(column=0, row=1, pady=10)

        ended = 1

    def coin_menu():
        # Clear all widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Create a new frame for the "Goals" section
        goals_frame = ttk.Frame(root, padding="3 3 12 12")
        goals_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Add the "Check goal" and "Edit goal" buttons
        ttk.Button(goals_frame, text='Show description', command=coin_desc).grid(column=0, row=1)
        ttk.Button(goals_frame, text='Run program', command=run_coin).grid(column=1, row=1)
        ttk.Button(goals_frame, text="Back to menu", command=restart).grid(column=0, row=2, pady=10, columnspan=2)

        ttk.Label(goals_frame, text='Choose a function:').grid(column=0, row=0, columnspan=2, pady = 20, padx=20)

        # Add padding to all child widgets inside 'goals_frame'
        for child in goals_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def run_x_y():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window
        video_script_path = os.path.abspath("x_y_calc/x_y_calc.py")

        # Run the Python script
        os.system(f'python "{video_script_path}"')
        ended = 1
        

    def x_y_desc():
        global ended  # Declare 'ended' as a global variable

        # Clear all widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Create a new frame for the video description
        desc_frame = ttk.Frame(root, padding="3 3 12 12")
        desc_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Read the content of 'video_desc.txt'
        with open('x_y_calc/x_y_desc.txt', 'r') as file:
            text = file.read()  # Read the file content as a string

        # Create a label to display the text
        ttk.Label(desc_frame, text=text, wraplength=400).grid(column=0, row=0, padx=10, pady=10)

        # Add a close button to return to the main menu
        ttk.Button(desc_frame, text="Close", command=restart).grid(column=0, row=1, pady=10)

        ended = 1

    def x_y_menu():
        # Clear all widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Create a new frame for the "Goals" section
        goals_frame = ttk.Frame(root, padding="3 3 12 12")
        goals_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Add the "Check goal" and "Edit goal" buttons
        ttk.Button(goals_frame, text='Show description', command=x_y_desc).grid(column=0, row=1)
        ttk.Button(goals_frame, text='Run program', command=run_x_y).grid(column=1, row=1)
        ttk.Button(goals_frame, text="Back to menu", command=restart).grid(column=0, row=2, pady=10, columnspan=2)

        ttk.Label(goals_frame, text='Choose a function:').grid(column=0, row=0, columnspan=2, pady = 20, padx=20)

        # Add padding to all child widgets inside 'goals_frame'
        for child in goals_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    


    def run_vertex():
        global ended  # Declare 'ended' as a global variable
        root.destroy()  # Close the current window
        video_script_path = os.path.abspath("Vertex/vertex.py")

        # Run the Python script
        os.system(f'python "{video_script_path}"')
        ended = 1
        

    def vertex_desc():
        global ended  # Declare 'ended' as a global variable

        # Clear all widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Create a new frame for the video description
        desc_frame = ttk.Frame(root, padding="3 3 12 12")
        desc_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Read the content of 'video_desc.txt'
        with open('Vertex/vertex_desc.txt', 'r') as file:
            text = file.read()  # Read the file content as a string

        # Create a label to display the text
        ttk.Label(desc_frame, text=text, wraplength=400).grid(column=0, row=0, padx=10, pady=10)

        # Add a close button to return to the main menu
        ttk.Button(desc_frame, text="Close", command=restart).grid(column=0, row=1, pady=10)

        ended = 1

    def vertex_menu():
        # Clear all widgets in the root window
        for widget in root.winfo_children():
            widget.destroy()

        # Create a new frame for the "Goals" section
        goals_frame = ttk.Frame(root, padding="3 3 12 12")
        goals_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Add the "Check goal" and "Edit goal" buttons
        ttk.Button(goals_frame, text='Show description', command=vertex_desc).grid(column=0, row=1)
        ttk.Button(goals_frame, text='Run program', command=run_vertex).grid(column=1, row=1)
        ttk.Button(goals_frame, text="Back to menu", command=restart).grid(column=0, row=2, pady=10, columnspan=2)

        ttk.Label(goals_frame, text='Choose a function:').grid(column=0, row=0, columnspan=2, pady = 20, padx=20)

        # Add padding to all child widgets inside 'goals_frame'
        for child in goals_frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    # Create a main frame inside the window with padding
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    # Configure resizing behavior
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Create buttons for the main menu
    ttk.Button(mainframe, text='Youtube mp4 downloader', command=video_menu).grid(column=1, row=2)
    ttk.Button(mainframe, text='Battle simulator', command=battle_menu).grid(column=2, row=2)
    ttk.Button(mainframe, text='Nat geo text downloader', command=nat_menu).grid(column=3, row=2)
    ttk.Button(mainframe, text='Coin change problem', command=coin_menu).grid(column=1, row=3)
    ttk.Button(mainframe, text='X and y calculator', command=x_y_menu).grid(column=2, row=3)
    ttk.Button(mainframe, text='Vertex form', command=vertex_menu).grid(column=3, row=3)
    ttk.Button(mainframe, text='Close', command=end_program).grid(column=1, row=8, columnspan=2)

    # Add a label for user instructions
    ttk.Label(mainframe, text='Please choose a function:').grid(column=1, row=1, columnspan=2, pady = 20, padx=20)

    # Add padding to all child widgets inside 'mainframe'
    for child in mainframe.winfo_children():
        child.grid_configure(padx=10, pady=10)

    # Start the Tkinter event loop
    root.mainloop()
    return ended


if __name__ == "__main__":
    while ended == 0:
        ended = main()  # Call the main function to run the application

#VJ, Battle Simulator
'''


Library Integration:

    Use Matplotlib for character stat visualizations
    Use Pandas for data manipulation and basic statistical analysis
    Use Faker for generating random character names and descriptions

Character Visualization:

    Create a radar chart or bar graph to display a character's stats using Matplotlib

Data Analysis:

    Use Pandas to load character data into a DataFrame
    Implement basic statistical analysis on character attributes (e.g., mean, median, max, min)

Random Generation:

    Use Faker to generate random character names and backstories

Enhanced User Interface:

    Create a menu system that allows users to access new visualization and analysis features

Documentation Reading:

    Demonstrate understanding of library documentation by implementing at least one additional feature from each library not explicitly required above


'''
import os
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from games import BattleSimulator
from profile_manager import ProfileManager
import matplotlib.pyplot as plt
from faker import Faker
import random
import csv


def pandas_data_analysis():
    '''Perform basic statistical analysis on character attributes using Pandas.'''
    file_path = os.path.join(os.path.dirname(__file__), 'profiles.csv')
    try:
        # Load profiles into a Pandas DataFrame
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        messagebox.showerror('Error', 'profiles.csv not found!')
        return

    # Perform statistical analysis
    stats = df[['DAMAGE', 'ARMOUR', 'DODGE', 'HEALTH', 'REGEN']].describe()

    # Create a new tkinter window
    analysis_window = tk.Toplevel()
    analysis_window.title('Statistical Analysis')

    # Add user-friendly labels
    user_friendly_stats = (
        f"Statistical Analysis of EVERY Character's Attributes:\n\n"
        f"Mean:\n{stats.loc['mean']}\n\n"
        f"Median:\n{df[['DAMAGE', 'ARMOUR', 'DODGE', 'HEALTH', 'REGEN']].median()}\n\n"
        f"Maximum:\n{stats.loc['max']}\n\n"
        f"Minimum:\n{stats.loc['min']}\n"
    )

    # Display the analysis in a Text widget
    text_widget = tk.Text(analysis_window, height=20, width=80)
    text_widget.pack(padx=10, pady=10)
    text_widget.insert(tk.END, user_friendly_stats)
    text_widget.config(state=tk.DISABLED)  # Make the text widget read-only

def matplotlib_display_pie_chart():
    """Display a pie chart of a character's stats using Matplotlib."""
    file_path = os.path.join(os.path.dirname(__file__), 'profiles.csv')
    try:
        # Load profiles into a Pandas DataFrame
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        messagebox.showerror('Error', 'profiles.csv not found!')
        return

    # Create a new tkinter window to select a character
    selection_window = tk.Toplevel()
    selection_window.title('Select Character for Pie Chart')

    tk.Label(selection_window, text='Select a Character:').pack(pady=5)

    # Create a Listbox to display character names
    character_listbox = tk.Listbox(selection_window, height=10, width=50)
    character_listbox.pack(pady=5)

    # Populate the Listbox with character names
    for name in df['NAME']:
        character_listbox.insert(tk.END, name)

    def generate_pie_chart():
        # Get the selected character
        selected_index = character_listbox.curselection()
        if not selected_index:
            messagebox.showerror('Error', 'Please select a character!')
            return

        character_name = df['NAME'].iloc[selected_index[0]]

        # Filter the DataFrame for the selected character
        character_data = df[df['NAME'] == character_name]

        # Extract stats for the character
        stats = ['DAMAGE', 'ARMOUR', 'DODGE', 'HEALTH', 'REGEN']
        values = character_data[stats].iloc[0].tolist()

        # Calculate the total points
        total_points = sum(values)

        # Create a pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(values, labels=stats, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
        plt.title(f'Stat Proportions for {character_name}\nTotal Points: {total_points}')
        plt.show()

        # Close the selection window after generating the chart
        selection_window.destroy()

    tk.Button(selection_window, text='Generate Pie Chart', command=generate_pie_chart).pack(pady=10)

def generate_random_character():
    '''Generate a random character name and class using Faker.'''
    fake = Faker()
    file_path = os.path.join(os.path.dirname(__file__), 'profiles.csv')

    # Define base stats for each class (matching profile_manager.py)
    base_stats = {
        'Warrior': {'DAMAGE': 14, 'ARMOUR': 24, 'DODGE': 1, 'HEALTH': 34, 'REGEN': 0},
        'Scout': {'DAMAGE': 18, 'ARMOUR': 0, 'DODGE': 34, 'HEALTH': 14, 'REGEN': 5},
        'Medic': {'DAMAGE': 10, 'ARMOUR': 4, 'DODGE': 10, 'HEALTH': 40, 'REGEN': 21},
        'Demoman': {'DAMAGE': 32, 'ARMOUR': 32, 'DODGE': 0, 'HEALTH': 4, 'REGEN': 0},
        'Kid': {'DAMAGE': random.randint(1,20), 'ARMOUR': random.randint(0,99), 'DODGE': random.randint(0,99), 'HEALTH': random.randint(0,25), 'REGEN': random.randint(0,99)}
    }

    # Generate a random character name and class
    character_name = fake.first_name()
    character_class = random.choice(list(base_stats.keys()))

    # Retrieve base stats for the selected class
    stats = base_stats[character_class]
    damage = stats['DAMAGE']
    armour = stats['ARMOUR']
    dodge = stats['DODGE']
    health = stats['HEALTH']
    regen = stats['REGEN']

    # Append the new character to the CSV file
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([character_name, character_class, damage, armour, dodge, health, regen])

    messagebox.showinfo('Success', f'Character {character_name} ({character_class}) added successfully!')

def main(repeat):
    while repeat > 0:
        # Create the main application window
        root = tk.Tk()
        root.title('Battle Simulator')

        # Functions for menu options
        def ply_game():
            root.destroy()  # Close the main menu window
            simulator = BattleSimulator()  # Instantiate the BattleSimulator class
            simulator.run()  # Run the game

        def mke_profile():
            """Return to the main menu."""
            root.destroy()  # Close the current window
            main(1)  # Restart the main menu

        def end_program():
            nonlocal repeat  # Use the nonlocal keyword to modify the outer variable
            repeat = 0  # Set repeat to 0 to end the program
            root.destroy()  # Close the current window

        # Create a main frame inside the window with padding
        mainframe = ttk.Frame(root, padding='3 3 12 12')
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

        # Configure resizing behavior
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Create buttons for different options
        ttk.Button(mainframe, text='Play Game', command=ply_game).grid(column=1, row=2, sticky=tk.W)
        ttk.Button(mainframe, text='Generate Random Character', command=generate_random_character).grid(column=1, row=3, sticky=tk.W)
        ttk.Button(mainframe, text='View Stats (Pandas)', command=pandas_data_analysis).grid(column=2, row=2, sticky=tk.W)
        ttk.Button(mainframe, text='View Stats (Graph)', command=matplotlib_display_pie_chart).grid(column=2, row=3, sticky=tk.W)
        ttk.Button(mainframe, text='Close', command=end_program).grid(column=2, row=8, sticky=tk.N)

        # Create label for user instructions
        ttk.Label(mainframe, text='Please choose a function:').grid(column=2, row=1, sticky=tk.W)

        # Add padding to all child widgets inside 'mainframe' for better spacing
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # Set the default window size
        root.geometry('450x300')

        # Start the Tkinter event loop
        root.mainloop()

    return repeat  # Return the repeat variable to indicate the program has ended


if __name__ == '__main__':
    repeat = 1
    while repeat > 0:
        repeat = main(repeat)
    print('Goodbye!!!')
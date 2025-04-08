import csv
import random
import pandas as pd
import tkinter as tk
from tkinter import messagebox


class ProfileManager:
    def __init__(self, root):
        self.root = root
        self.root.title('Profile Manager')
        self.character_name = tk.StringVar()
        self.class_choice = tk.StringVar()
        self.data_frame = None

        # Create UI elements
        self.create_ui()

    def create_ui(self):
        # Character selection
        tk.Label(self.root, text='Enter Character Name:').grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(self.root, textvariable=self.character_name).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.root, text='Select Character', command=self.select_character).grid(row=0, column=2, padx=10, pady=5)

        # Display DataFrame
        self.data_frame = tk.Text(self.root, height=15, width=80, state=tk.DISABLED)
        self.data_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Create new profile
        tk.Button(self.root, text='Create New Profile', command=self.create_profile_ui).grid(row=2, column=0, columnspan=3, pady=10)

    def load_profiles(self):
        # Load profiles from CSV
        data = {
            'Name': [],
            'Class': [],
            'Damage': [],
            'Armour': [],
            'Dodge': [],
            'Health': [],
            'Regen': []
        }
        try:
            with open('Battle Simulator Update/profiles.csv', 'r') as file:
                read = csv.reader(file)
                next(read)
                for row in read:
                    data['Name'].append(row[0])
                    data['Class'].append(row[1])
                    data['Damage'].append(int(row[2]))
                    data['Armour'].append(int(row[3]))
                    data['Dodge'].append(int(row[4]))
                    data['Health'].append(int(row[5]))
                    data['Regen'].append(int(row[6]))
        except FileNotFoundError:
            messagebox.showerror('Error', 'profiles.csv not found!')
            return None

        return pd.DataFrame(data)

    def display_profiles(self):
        # Display profiles in the text widget
        df = self.load_profiles()
        if df is not None:
            self.data_frame.config(state=tk.NORMAL)
            self.data_frame.delete(1.0, tk.END)
            self.data_frame.insert(tk.END, df.to_string(index=False))
            self.data_frame.config(state=tk.DISABLED)

    def select_character(self):
        # Select a character by name
        name = self.character_name.get().strip()
        if not name:
            messagebox.showwarning('Warning', 'Please enter a character name!')
            return

        df = self.load_profiles()
        if df is not None:
            character = df[df['Name'].str.lower() == name.lower()]
            if character.empty:
                messagebox.showinfo('Info', f'Character "{name}" not found. Creating a new profile.')
                self.create_profile_ui(name)
            else:
                stats = character.iloc[0].to_dict()
                messagebox.showinfo('Character Stats', '\n'.join([f'{key}: {value}' for key, value in stats.items()]))

    def create_profile_ui(self, name=None):
        # Create a new profile
        create_window = tk.Toplevel(self.root)
        create_window.title('Create Profile')

        tk.Label(create_window, text='Enter Character Name:').grid(row=0, column=0, padx=10, pady=5)
        name_entry = tk.Entry(create_window)
        name_entry.grid(row=0, column=1, padx=10, pady=5)
        if name:
            name_entry.insert(0, name)

        tk.Label(create_window, text='Choose Class:').grid(row=1, column=0, padx=10, pady=5)
        class_var = tk.StringVar(value='1')
        classes = [
            ('Warrior', 1),
            ('Scout', 2),
            ('Medic', 3),
            ('Demoman', 4),
            ('Kid', 5)
        ]
        for i, (text, value) in enumerate(classes):
            tk.Radiobutton(create_window, text=text, variable=class_var, value=value).grid(row=2 + i, column=0, columnspan=2, sticky='w', padx=10)

        def save_profile():
            char_name = name_entry.get().strip().upper()
            if not char_name:
                messagebox.showwarning('Warning', 'Character name cannot be empty!')
                return

            class_choice = int(class_var.get())
            if class_choice == 1:
                clss, damage, armour, dodge, health, regen = 'Warrior', 14, 24, 1, 34, 0
            elif class_choice == 2:
                clss, damage, armour, dodge, health, regen = 'Scout', 18, 0, 34, 14, 5
            elif class_choice == 3:
                clss, damage, armour, dodge, health, regen = 'Medic', 10, 4, 10, 40, 21
            elif class_choice == 4:
                clss, damage, armour, dodge, health, regen = 'Demoman', 32, 32, 0, 4, 0
            elif class_choice == 5:
                clss, damage, armour, dodge, health, regen = 'Kid', random.randint(0,20), random.randint(0,99), random.randint(0,99), random.randint(0,25), random.randint(0,99)

            profile = [char_name, clss, damage, armour, dodge, health, regen]

            try:
                with open('Battle Simulator Update/profiles.csv', 'a', newline='') as file:
                    writer = csv.writer(file, lineterminator='\n')
                    writer.writerow(profile)
                messagebox.showinfo('Success', f'Profile for "{char_name}" created successfully!')
                create_window.destroy()
                self.display_profiles()
            except Exception as e:
                messagebox.showerror('Error', f'Failed to save profile: {e}')

        tk.Button(create_window, text='Save Profile', command=save_profile).grid(row=7, column=0, columnspan=2, pady=10)

        self.display_profiles()


if __name__ == '__main__':
    root = tk.Tk()
    app = ProfileManager(root)
    app.display_profiles()
    root.mainloop()

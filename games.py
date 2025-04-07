import tkinter as tk
import random
import os
import csv
from profile_manager import ProfileManager


class BattleSimulator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Battle Simulator')

        self.text_display = tk.Text(self.root, height=20, width=50, state=tk.DISABLED)
        self.text_display.pack()

        self.game_button = tk.Button(self.root, text='Start Game', command=self.start_game)
        self.game_button.pack()

        self.menu_button = tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu)
        self.menu_button.pack()

        self.continue_button = None
        self.valid_prfl = None
        self.enmy_prfl = None
        self.base_prfl = None
        self.enmy_base_prfl = None
        self.win = 1
        self.turn = 1

    def update_display(self, text):
        self.text_display.config(state=tk.NORMAL)
        self.text_display.insert(tk.END, text + '\n')
        self.text_display.config(state=tk.DISABLED)

    def load_profiles(self):
        # Load profiles from the CSV file
        profiles = []
        file_path = os.path.join(os.path.dirname(__file__), 'profiles.csv')  # Updated file path
        try:
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    # Convert numeric fields to integers
                    profiles.append([
                        row[0],  # Name
                        row[1],  # Class
                        int(row[2]),  # Damage
                        int(row[3]),  # Armour
                        min(int(row[4]), 99),  # Dodge (capped at 99)
                        int(row[5]),  # Health
                        min(int(row[6]), 99)   # Regen (capped at 99)
                    ])
        except FileNotFoundError:
            self.update_display('Error: profiles.csv not found. Please create profiles first.')
            return None
        return profiles

    def start_game(self):
        # Hide the Start Game and Back to Menu buttons
        self.game_button.pack_forget()
        self.menu_button.pack_forget()

        profiles = self.load_profiles()
        if not profiles:
            self.update_display('No profiles found. Please create profiles first.')
            return

        self.select_player_profile(profiles)

    def select_player_profile(self, profiles):
        # Allow the player to select their profile
        def set_profile():
            selected_index = profile_listbox.curselection()
            if not selected_index:
                self.update_display('Please select a profile!')
                return
            self.valid_prfl = profiles[selected_index[0]]
            self.base_prfl = self.valid_prfl[:]
            profiles.pop(selected_index[0])  # Remove the selected profile from the list
            self.enmy_prfl = random.choice(profiles)  # Randomly select an enemy profile
            self.enmy_base_prfl = self.enmy_prfl[:]
            selection_window.destroy()
            self.update_display(f'Player Profile: {self.valid_prfl[0]}')
            self.update_display(f'Enemy Profile: {self.enmy_prfl[0]}')
            self.cmbt()  # Start the combat after profile selection

        # Create a selection window
        selection_window = tk.Toplevel(self.root)
        selection_window.title('Select Your Profile')

        tk.Label(selection_window, text='Select Your Profile:').pack(pady=5)
        profile_listbox = tk.Listbox(selection_window, height=10, width=50)
        profile_listbox.pack(pady=5)

        for profile in profiles:
            profile_listbox.insert(tk.END, f'{profile[0]} - {profile[1]}')

        tk.Button(selection_window, text='Select', command=set_profile).pack(pady=5)

    def cmbt(self):
        if self.turn == 1:
            self.update_display('\nYour turn\n')
            self.create_continue_button()
            if self.combat_turn(self.valid_prfl, self.enmy_prfl, self.enmy_base_prfl):
                self.update_display('You won!')
                self.upgrade_stats()  # Call the upgrade stats method after winning
                return
            self.turn = 2
        else:
            self.update_display('\nEnemy turn\n')
            self.create_continue_button()
            if self.combat_turn(self.enmy_prfl, self.valid_prfl, self.base_prfl):
                self.update_display('You lost!')
                self.end_game()
                return
            self.turn = 1

    def combat_turn(self, attacker, defender, base_defender):
        if random.randint(0, 100) <= attacker[6]:  # Healing
            heal = random.randint(4, 10)
            attacker[5] = min(attacker[5] + heal, base_defender[5])
            self.update_display(f'{attacker[0]} healed {heal} HP, health is now {attacker[5]}')

        damage = attacker[2]
        if random.randint(1, 5) <= 2:  # Indirect hit
            damage = round(damage * random.uniform(0.25, 0.75))
            self.update_display('Indirect hit, damage reduced')

        if random.randint(0, 100) <= defender[4]:  # Dodge
            self.update_display(f'{defender[0]} dodged the attack!')
            damage = 0

        if random.randint(0, 100) <= defender[3]:  # Armour
            damage = round(damage * random.uniform(0, 0.8))
            self.update_display(f'{defender[0]}\'s armour reduced damage!')

        defender[5] -= damage
        self.update_display(f'{defender[0]} took {damage} damage! Health is now {defender[5]}')

        return defender[5] <= 0  # Return True if defender is defeated

    def upgrade_stats(self):
        # Allow the player to upgrade their stats
        def upgrade(stat_index, stat_name):
            if stat_name in ['Dodge', 'Regen']:
                self.valid_prfl[stat_index] = min(self.valid_prfl[stat_index] + 3, 99)  # Cap at 99
            else:
                self.valid_prfl[stat_index] += 3
            self.update_display(f'{stat_name} increased to {self.valid_prfl[stat_index]}!')
            self.save_profile()  # Save the updated profile
            upgrade_window.destroy()  # Close the upgrade window
            self.restart_main_menu()  # Return to the main menu

        # Create buttons for upgrading stats
        upgrade_window = tk.Toplevel(self.root)
        upgrade_window.title('Upgrade Stats')

        tk.Label(upgrade_window, text='Choose a stat to upgrade:').pack(pady=5)

        tk.Button(upgrade_window, text='Damage', command=lambda: upgrade(2, 'Damage')).pack(pady=5)
        tk.Button(upgrade_window, text='Armour', command=lambda: upgrade(3, 'Armour')).pack(pady=5)
        tk.Button(upgrade_window, text='Dodge', command=lambda: upgrade(4, 'Dodge')).pack(pady=5)
        tk.Button(upgrade_window, text='Health', command=lambda: upgrade(5, 'Health')).pack(pady=5)
        tk.Button(upgrade_window, text='Regen', command=lambda: upgrade(6, 'Regen')).pack(pady=5)

    def save_profile(self):
        """Save the updated profile to the CSV file."""
        file_path = os.path.join(os.path.dirname(__file__), 'profiles.csv')
        profiles = self.load_profiles()

        # Check if the character already exists in the profiles
        for i, profile in enumerate(profiles):
            if profile[0].upper() == self.valid_prfl[0].upper():  # Match by character name (case-insensitive)
                profiles[i] = self.valid_prfl  # Overwrite the existing profile
                break
        else:
            # If the character does not exist, append it as a new profile
            profiles.append(self.valid_prfl)

        # Write the updated profiles back to the CSV file
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['NAME', 'CLASS', 'DAMAGE', 'ARMOUR', 'DODGE', 'HEALTH', 'REGEN'])
            writer.writerows(profiles)

    def end_game(self):
        # Disable further actions and display a message
        self.update_display('Game Over! Restart the application to play again.')
        if self.continue_button:
            self.continue_button.pack_forget()

    def restart_main_menu(self):
        """Return to the main menu."""
        self.root.destroy()  # Close the current game window
        from main import main  # Import the main menu function
        main(1)  # Restart the main menu

    def create_continue_button(self):
        """Create a Continue button to proceed to the next turn."""
        if self.continue_button:
            self.continue_button.pack_forget()  # Remove the previous button if it exists

        self.continue_button = tk.Button(self.root, text='Continue', command=self.next_turn)
        self.continue_button.pack()

    def next_turn(self):
        """Handle the logic for proceeding to the next turn."""
        if self.continue_button:
            self.continue_button.pack_forget()  # Remove the Continue button
        self.update_display('Proceeding to the next turn...')
        self.cmbt()  # Call the combat method to continue the game

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    BattleSimulator().run()
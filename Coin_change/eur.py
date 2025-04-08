import tkinter as tk
from tkinter import ttk
import csv

class EUR():
    def __init__(self, root):
        self.root = root
        self.amount = tk.StringVar()
        self.tot = {
        }
        with open('Coin_change_problem/eur.csv', 'r') as file:
            reader = csv.reader(file)
            self.whole = [row for row in reader]
        for item in self.whole:
            self.tot.update({item[0].strip():float(item[1])})
        self.result = tk.StringVar()

        self.validate_cmd = (self.root.register(self.validate_float), "%P")

        # UI setup
        tk.Label(self.root, text='Enter amount in EUR:').grid(row=0, column=0, pady=5, sticky='e')
        tk.Entry(self.root, textvariable=self.amount, validate="key", validatecommand=self.validate_cmd).grid(row=0, column=1, pady=5, sticky='w')
        tk.Button(self.root, text='Calculate', command=self.calculate_currency).grid(row=1, column=0, columnspan=2, pady=10)
        tk.Label(self.root, text='Result:').grid(row=2, column=0, pady=5, sticky='ne')
        tk.Label(self.root, textvariable=self.result, justify='left').grid(row=2, column=1, pady=5, sticky='w')

        tk.Button(self.root, text='Back to Menu', command=self.restart_main_menu).grid(row=3, column=0, columnspan=2, pady=20)

        # Handle window close event
        self.root.protocol("WM_DELETE_WINDOW", self.restart_main_menu)

    def validate_float(self, value):
        """Validate that the input is a valid float."""
        if value == "" or value.replace(".", "", 1).isdigit():
            return True
        return False

    def calculate_currency(self):
        """Calculate the breakdown of the amount into currency denominations."""
        try:
            amount = float(self.amount.get())
            breakdown = []
            for denom, value in self.tot.items():
                count = int(amount // value)
                if count > 0:
                    breakdown.append(f"{count} {denom}")
                    amount = round(amount % value, 2)  # Avoid floating-point precision issues
            self.result.set("\n".join(breakdown) if breakdown else "No currency needed.")
        except ValueError:
            self.result.set("Invalid input. Please enter a valid number.")

    def restart_main_menu(self):
        """Return to the main menu."""
        self.root.destroy()  # Close the current game window
        from Coin_change.main_coin import main  # Import the main menu function
        main()  # Restart the main menu
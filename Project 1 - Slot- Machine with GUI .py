import tkinter as tk
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(lines + 1)

    return winnings, winnings_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def spin():
    lines = int(lines_entry.get())
    bet = int(bet_entry.get())
    total_bet = bet * lines

    if total_bet > balance:
        result_label.configure(text="You do not have enough to bet that amount.")
        return

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    display_slot_machine(slots)

    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    result_label.configure(text=f"You won ${winnings}.")
    result_lines_label.configure(text="You won on lines: " + ", ".join(map(str, winnings_lines)))

    update_balance(winnings - total_bet)

def update_balance(amount):
    global balance
    balance += amount
    balance_label.configure(text=f"Current balance: ${balance}")

def deposit():
    amount = int(deposit_entry.get())
    update_balance(amount)
    deposit_entry.delete(0, tk.END)

def display_slot_machine(columns):
    for row in range(ROWS):
        for i, column in enumerate(columns):
            slot_label = tk.Label(slots_frame, text=column[row], width=5, relief="solid")
            slot_label.grid(row=row, column=i, padx=5, pady=5)

# Create the main Tkinter window
root = tk.Tk()
root.title("Slot Machine Game")

# Create and position GUI elements
balance = 0
balance_label = tk.Label(root, text="Current balance: $0")
balance_label.pack()

deposit_label = tk.Label(root, text="Deposit amount:")
deposit_label.pack()
deposit_entry = tk.Entry(root)
deposit_entry.pack()
deposit_button = tk.Button(root, text="Deposit", command=deposit)
deposit_button.pack()

lines_label = tk.Label(root, text="Number of lines (1-" + str(MAX_LINES) + "):")
lines_label.pack()
lines_entry = tk.Entry(root)
lines_entry.pack()

bet_label = tk.Label(root, text="Bet amount ($" + str(MIN_BET) + "-" + str(MAX_BET) + "):")
bet_label.pack()
bet_entry = tk.Entry(root)
bet_entry.pack()

spin_button = tk.Button(root, text="Spin", command=spin)
spin_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

result_lines_label = tk.Label(root, text="")
result_lines_label.pack()

# Create a frame to hold the slot machine columns
slots_frame = tk.Frame(root)
slots_frame.pack()

# Run the Tkinter event loop
root.mainloop()

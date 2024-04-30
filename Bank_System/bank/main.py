import sqlite3
import tkinter as tk
from tkinter import ttk

# Create a SQLite database and table
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        account_number INTEGER PRIMARY KEY,
        account_holder TEXT,
        balance REAL
    )
''')
conn.commit()

window = tk.Tk()
window.title("Bank Account System")
window.geometry('602x461')
# window.resizable(0, 0)


result_text = ttk.Treeview(columns=("account_number", "account_holder", "balance"), show="headings")
result_text.grid(row=10, column=0, columnspan=2)
result_text.heading("account_number", text="account_number")
result_text.heading("account_holder", text="account_holder")
result_text.heading("balance", text="balance")


def show_accounts():
    result_text.delete(*result_text.get_children())
    cursor.execute("SELECT * FROM accounts")
    for row in cursor.fetchall():
        result_text.insert("", "end", values=row)


show_accounts()


# Function to create a new account
def create_account():
    account_number = account_number_entry.get()
    account_holder = account_holder_entry.get()
    cursor.execute("INSERT INTO accounts VALUES (?, ?, 0.0)", (account_number, account_holder))
    conn.commit()
    status_label.config(text="Account created successfully.")
    show_accounts()


# Function to deposit into an account
def deposit():
    account_number = result_text.selection()
    amount = float(deposit_amount_entry.get())
    if account_number:
        account_number = result_text.item(account_number, 'values')[0]
        cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_number = ?", (amount, account_number))
        conn.commit()
        status_label.config(text="Deposit successful.")
    show_accounts()


# Function to withdraw from an account
def withdraw():
    account_number = result_text.selection()
    amount = float(withdraw_amount_entry.get())
    if account_number:
        account_number = result_text.item(account_number, 'values')[0]
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_number = ?", (amount, account_number))
        conn.commit()
        status_label.config(text="Withdrawal successful.")
    show_accounts()


# Function to delete an account
def delete_account():
    selected_item = result_text.selection()
    if selected_item:
        account_number = result_text.item(selected_item, 'values')[0]
        cursor.execute("DELETE FROM accounts WHERE account_number=?", (account_number,))
        conn.commit()
    status_label.config(text="Account deleted.")
    show_accounts()


# Create the main window


# Create and layout widgets
account_number_label = tk.Label(window, text="Account Number:")
account_number_label.grid(row=0, column=0)
account_number_entry = tk.Entry(window)
account_number_entry.grid(row=0, column=0, columnspan=2)

account_holder_label = tk.Label(window, text="Account Holder:")
account_holder_label.grid(row=1, column=0)
account_holder_entry = tk.Entry(window)
account_holder_entry.grid(row=1, column=0, columnspan=2)

create_account_button = tk.Button(window, text="Create Account", command=create_account)
create_account_button.grid(row=2, column=0, columnspan=2)

deposit_amount_label = tk.Label(window, text="Deposit Amount:")
deposit_amount_label.grid(row=3, column=0)
deposit_amount_entry = tk.Entry(window)
deposit_amount_entry.grid(row=3, column=0, columnspan=2)

deposit_button = tk.Button(window, text="Deposit", command=deposit)
deposit_button.grid(row=4, column=0, columnspan=2)

withdraw_amount_label = tk.Label(window, text="Withdraw Amount:")
withdraw_amount_label.grid(row=5, column=0)
withdraw_amount_entry = tk.Entry(window)
withdraw_amount_entry.grid(row=5, column=0, columnspan=2)

withdraw_button = tk.Button(window, text="Withdraw", command=withdraw)
withdraw_button.grid(row=6, column=0, columnspan=2)

# show_accounts_button = tk.Button(window, text="Show Accounts", command=show_accounts)
# show_accounts_button.grid(row=7, column=0, columnspan=2)

delete_account_button = tk.Button(window, text="Delete Account", command=delete_account)
delete_account_button.grid(row=8, column=0, columnspan=2)

status_label = tk.Label(window, text="")
status_label.grid(row=9, column=0, columnspan=2)

# result_text = tk.Text(window, state=tk.DISABLED, height=10, width=50)
# result_text.grid(row=10, column=0, columnspan=2)

window.mainloop()

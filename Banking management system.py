import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ---------------- DATABASE ----------------
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers(
    account_no INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    balance REAL
)
""")
conn.commit()


# ---------------- FUNCTIONS ----------------
def add_customer():
    name = name_entry.get()
    phone = phone_entry.get()
    balance = balance_entry.get()

    if name == "" or phone == "" or balance == "":
        messagebox.showerror("Error", "Fill all fields")
        return

    cursor.execute(
        "INSERT INTO customers(name, phone, balance) VALUES(?,?,?)",
        (name, phone, float(balance))
    )
    conn.commit()

    messagebox.showinfo("Success", "Customer Added")

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    balance_entry.delete(0, tk.END)

    show_data()


def show_data():
    for row in tree.get_children():
        tree.delete(row)

    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", tk.END, values=row)


# ---------------- GUI ----------------
root = tk.Tk()
root.title("Banking Management System")
root.geometry("700x500")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Opening Balance").pack()
balance_entry = tk.Entry(root)
balance_entry.pack()

tk.Button(root, text="Add Customer", command=add_customer).pack(pady=10)

columns = ("Account No", "Name", "Phone", "Balance")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)

tree.pack(fill="both", expand=True)

show_data()

root.mainloop()

conn.close()
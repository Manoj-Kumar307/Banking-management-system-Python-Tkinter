# Banking Management System

A desktop banking application built with **Python (Tkinter)** for the GUI and **SQLite** for persistent storage. Lets you onboard new customers, store their details, and view all accounts in a live table.

## Features
- Add new customers (name, phone number, opening balance)
- Input validation with popup error/success messages
- Auto-incrementing account numbers
- Data persisted in a local SQLite database (`bank.db`)
- Live table view (Treeview) that refreshes automatically after every update

## Tech Stack
- **Python 3**
- **Tkinter** — GUI
- **SQLite3** — database
- **ttk.messagebox** — validation dialogs

## How It Works
1. On launch, the app connects to (or creates) `bank.db` and ensures a `customers` table exists.
2. Fill in the Name, Phone, and Opening Balance fields and click **Add Customer**.
3. The app validates the fields, inserts the record using a parameterized SQL query, and refreshes the table.

## Getting Started

```bash
git clone https://github.com/Manoj-Kumar307/Banking-management-system-Python-Tkinter.git
cd Banking-management-system-Python-Tkinter
python "Banking management system.py"
```

No external packages required — `tkinter` and `sqlite3` ship with standard Python.

## Database Schema

```sql
CREATE TABLE customers(
    account_no INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    balance REAL
)
```

## Planned Improvements
- Withdraw / deposit / transfer functionality
- Search and edit existing customer records
- Delete/close account option
- Transaction history log

## Author
**Manoj Kumar J** — [GitHub](https://github.com/Manoj-Kumar307) · [LinkedIn](https://linkedin.com/in/manojkumar07060300304)

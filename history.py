from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Transaction History")
root.geometry("900x500")
root.config(bg="white")

heading = Label(
    root,
    text="Transaction History",
    font=("Arial", 28, "bold"),
    bg="white",
    fg="#003366"
)

heading.pack(pady=20)

table_frame = Frame(root, bg="white")
table_frame.pack(pady=20)

columns = ("Account No", "Name", "Type", "Amount", "Date")

tree = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=12
)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

data = [
    ("1001", "Aastha", "Deposit", "5000", "10-05-2026"),
    ("1002", "Rahul", "Withdraw", "2000", "11-05-2026"),
    ("1003", "Priya", "Deposit", "8000", "12-05-2026")
]

for row in data:
    tree.insert("", END, values=row)

tree.pack()

root.mainloop()
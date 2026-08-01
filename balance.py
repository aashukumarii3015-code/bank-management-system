from tkinter import *
from tkinter import messagebox
from database import *

root = Tk()
root.title("Balance Check")
root.geometry("500x300")

Label(root,text="BALANCE CHECK",font=("Arial",20,"bold")).pack(pady=20)

Label(root,text="Account Number",font=("Arial",12)).pack()
acc_entry = Entry(root,font=("Arial",12),width=30)
acc_entry.pack(pady=10)


def check_balance():
    acc_no = acc_entry.get()

    cursor.execute("SELECT balance FROM accounts WHERE acc_no=%s",(acc_no,))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Balance",f"Current Balance = ₹{result[0]}")
    else:
        messagebox.showerror("Error","Account Not Found")

Button(root,text="Check Balance",font=("Arial",14),bg="#003366",fg="white",
       command=check_balance).pack(pady=20)

root.mainloop()
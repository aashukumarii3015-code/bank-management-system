from tkinter import *
from tkinter import messagebox
from database import *

root = Tk()
root.title("Withdraw Money")
root.geometry("500x400")
root.config(bg="#fff0f0")

Label(root,text="WITHDRAW MONEY",font=("Arial",20,"bold"),bg="#fff0f0").pack(pady=20)

Label(root,text="Account Number",bg="#fff0f0",font=("Arial",12)).pack()
acc_entry = Entry(root,font=("Arial",12),width=30)
acc_entry.pack(pady=5)

Label(root,text="Amount",bg="#fff0f0",font=("Arial",12)).pack()
amount_entry = Entry(root,font=("Arial",12),width=30)
amount_entry.pack(pady=5)


def withdraw_money():
    acc_no = acc_entry.get()
    amount = float(amount_entry.get())

    cursor.execute("SELECT balance FROM accounts WHERE acc_no=%s",(acc_no,))
    balance = cursor.fetchone()[0]

    if balance >= amount:
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE acc_no=%s",
                       (amount,acc_no))

        cursor.execute("INSERT INTO transactions(acc_no,trans_type,amount) VALUES(%s,%s,%s)",
                       (acc_no,"Withdraw",amount))

        conn.commit()

root.mainloop()
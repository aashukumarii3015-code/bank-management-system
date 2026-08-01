from tkinter import *
from tkinter import messagebox
from database import *

root = Tk()
root.title("Deposit Money")
root.geometry("500x400")
root.config(bg="#e6fff2")

Label(root,text="DEPOSIT MONEY",font=("Arial",20,"bold"),bg="#e6fff2").pack(pady=20)

Label(root,text="Account Number",bg="#e6fff2",font=("Arial",12)).pack()
acc_entry = Entry(root,font=("Arial",12),width=30)
acc_entry.pack(pady=5)

Label(root,text="Amount",bg="#e6fff2",font=("Arial",12)).pack()
amount_entry = Entry(root,font=("Arial",12),width=30)
amount_entry.pack(pady=5)


def deposit_money():
    acc_no = acc_entry.get()
    amount = float(amount_entry.get())

    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE acc_no=%s",
                   (amount,acc_no))

    cursor.execute("INSERT INTO transactions(acc_no,trans_type,amount) VALUES(%s,%s,%s)",
                   (acc_no,"Deposit",amount))

    conn.commit()

    messagebox.showinfo("Success","Money Deposited")

Button(root,text="Deposit",font=("Arial",14),bg="green",fg="white",
       command=deposit_money).pack(pady=20)

root.mainloop()
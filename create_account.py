from tkinter import *

root = Tk()
root.title("Create Account")
root.geometry("500x400")

Label(root,
      text="CREATE ACCOUNT",
      font=("Arial",25,"bold")).pack(pady=30)

Label(root,text="Customer Name").pack()
Entry(root,width=30).pack(pady=10)

Label(root,text="Account Type").pack()
Entry(root,width=30).pack(pady=10)

Label(root,text="Opening Balance").pack()
Entry(root,width=30).pack(pady=10)

Button(root,
       text="Create Account",
       bg="green",
       fg="white",
       font=("Arial",14)).pack(pady=20)

root.mainloop()
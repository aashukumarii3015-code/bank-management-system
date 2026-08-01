import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
import datetime

# ================= DATABASE =================

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts(
    acc_no INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    acc_type TEXT,
    balance REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    acc_no INTEGER,
    type TEXT,
    amount REAL,
    date TEXT
)
""")

conn.commit()

# ================= MAIN WINDOW =================

root = Tk()
root.state("zoomed")
root.title("Royal Trust Bank")
root.config(bg="#EAF2FF")

# ================= COLORS =================

navy = "#002B5B"
blue = "#0A4D8C"
light = "#EAF2FF"
white = "white"
gold = "#F9A826"

# ================= NAVBAR =================

navbar = Frame(root, bg=navy, height=80)
navbar.pack(fill=X)

logo = Label(
    navbar,
    text="🏦 ROYAL TRUST BANK",
    font=("Arial", 30, "bold"),
    bg=navy,
    fg=white
)
logo.pack(side=LEFT, padx=30, pady=15)

# ================= SCROLLABLE CONTENT FRAME =================

main_canvas = Canvas(
    root,
    bg=light,
    highlightthickness=0
)

scrollbar = Scrollbar(
    root,
    orient=VERTICAL,
    command=main_canvas.yview
)
scrollbar.pack(side=RIGHT, fill=Y)

main_canvas.pack(side=LEFT, fill=BOTH, expand=True)
main_canvas.configure(yscrollcommand=scrollbar.set)

content_frame = Frame(
    main_canvas,
    bg=light
)

canvas_window = main_canvas.create_window(
    (0, 0),
    window=content_frame,
    anchor="nw"
)

def configure_scroll(event):
    main_canvas.configure(scrollregion=main_canvas.bbox("all"))

content_frame.bind("<Configure>", configure_scroll)

def configure_canvas_width(event):
    main_canvas.itemconfig(canvas_window, width=event.width)

main_canvas.bind("<Configure>", configure_canvas_width)

# ================= MOUSE SCROLL =================

def mouse_scroll(event):
    main_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

main_canvas.bind_all("<MouseWheel>", mouse_scroll)

# ================= SLIDER =================

slider_messages = [
    "Secure Digital Banking Experience",
    "Trusted By Thousands Of Customers",
    "Fast Transactions & Smart Banking"
]

slider_index = 0
slider_label = None

def start_slider():
    global slider_index
    if slider_label and slider_label.winfo_exists():
        slider_label.config(text=slider_messages[slider_index])
        slider_index = (slider_index + 1) % len(slider_messages)
        root.after(2000, start_slider)

# ================= CLEAR PAGE =================

def clear_page():
    for widget in content_frame.winfo_children():
        widget.destroy()

# ================= NAVIGATION PAGES =================

def about_page():
    clear_page()
    main_canvas.yview_moveto(0)
    
    box_wrapper = Frame(content_frame, bg=light)
    box_wrapper.pack(pady=80, expand=True)
    
    box = Frame(box_wrapper, bg=white, bd=3, relief=RIDGE)
    box.pack(ipadx=50, ipady=30)
    
    Label(box, text="About Us", font=("Arial", 30, "bold"), bg=white, fg=navy).pack(pady=20)
    
    about_text = ("Royal Trust Bank is a premier financial institution\n"
                  "dedicated to delivering secure, intelligent, and rapid\n"
                  "banking solutions for individuals and corporate entities worldwide.")
    
    Label(box, text=about_text, font=("Arial", 14), bg=white, fg="black", justify=CENTER).pack(pady=10)

def contact_page():
    clear_page()
    main_canvas.yview_moveto(0)
    
    box_wrapper = Frame(content_frame, bg=light)
    box_wrapper.pack(pady=80, expand=True)
    
    box = Frame(box_wrapper, bg=white, bd=3, relief=RIDGE)
    box.pack(ipadx=50, ipady=30)
    
    Label(box, text="Contact Us", font=("Arial", 30, "bold"), bg=white, fg=navy).pack(pady=20)
    Label(box, text="📧 Support: support@royaltrustbank.com", font=("Arial", 14), bg=white).pack(pady=5)
    Label(box, text="📞 Toll-Free: 1-800-123-4567", font=("Arial", 14), bg=white).pack(pady=5)

# ================= LOGIN PAGE =================

def login_page():
    clear_page()
    main_canvas.yview_moveto(0)

    box_wrapper = Frame(content_frame, bg=light)
    box_wrapper.pack(pady=80, expand=True)

    box = Frame(box_wrapper, bg=white, bd=3, relief=RIDGE)
    box.pack(ipadx=40, ipady=20)

    Label(box, text="Customer Login", font=("Arial", 30, "bold"), bg=white, fg=navy).pack(pady=25)

    Label(box, text="Customer Name", font=("Arial", 14), bg=white).pack(anchor="w", padx=60)
    name_entry = Entry(box, font=("Arial", 14), width=30)
    name_entry.pack(pady=10, padx=60)

    Label(box, text="Account Number", font=("Arial", 14), bg=white).pack(anchor="w", padx=60)
    acc_entry = Entry(box, font=("Arial", 14), width=30)
    acc_entry.pack(pady=10, padx=60)

    def verify():
        name = name_entry.get()
        acc = acc_entry.get()
        cursor.execute("SELECT * FROM accounts WHERE acc_no=? AND name=?", (acc, name))
        if cursor.fetchone():
            messagebox.showinfo("Success", "Login Successful")
            home_page()
        else:
            messagebox.showerror("Error", "Invalid Details")

    Button(box, text="Login", font=("Arial", 15, "bold"), bg=navy, fg=white, width=18, command=verify).pack(pady=30)

# ================= SERVICE INTERFACES =================

def create_account_page():
    clear_page()
    main_canvas.yview_moveto(0)
    
    box_wrapper = Frame(content_frame, bg=light)
    box_wrapper.pack(pady=60, expand=True)
    
    box = Frame(box_wrapper, bg=white, bd=3, relief=RIDGE)
    box.pack(ipadx=40, ipady=20)
    
    Label(box, text="Create New Account", font=("Arial", 26, "bold"), bg=white, fg=navy).pack(pady=20)
    
    Label(box, text="Full Name", font=("Arial", 14), bg=white).pack(anchor="w", padx=60)
    name_entry = Entry(box, font=("Arial", 14), width=30)
    name_entry.pack(pady=8, padx=60)
    
    Label(box, text="Account Type", font=("Arial", 14), bg=white).pack(anchor="w", padx=60)
    type_combo = ttk.Combobox(box, values=["Savings", "Current"], font=("Arial", 14), width=28, state="readonly")
    type_combo.set("Savings")
    type_combo.pack(pady=8, padx=60)
    
    Label(box, text="Initial Deposit Balance", font=("Arial", 14), bg=white).pack(anchor="w", padx=60)
    bal_entry = Entry(box, font=("Arial", 14), width=30)
    bal_entry.pack(pady=8, padx=60)
    
    def submit():
        name = name_entry.get().strip()
        acc_type = type_combo.get()
        bal_str = bal_entry.get().strip()
        
        if not name or not bal_str:
            messagebox.showerror("Error", "All fields are required")
            return
        try:
            balance = float(bal_str)
            if balance < 0: raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric starting balance")
            return
            
        cursor.execute("INSERT INTO accounts (name, acc_type, balance) VALUES (?, ?, ?)", (name, acc_type, balance))
        new_id = cursor.lastrowid
        
        if balance > 0:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO transactions (acc_no, type, amount, date) VALUES (?, 'Deposit', ?, ?)", (new_id, balance, now))
            
        conn.commit()
        messagebox.showinfo("Success", f"Account Successfully Created!\nYour Generated Account Number is: {new_id}")
        home_page()

    Button(box, text="Register Account", font=("Arial", 14, "bold"), bg=navy, fg=white, width=20, command=submit).pack(pady=20)
    Button(box, text="← Back to Home", font=("Arial", 12), bg="gray", fg=white, width=15, bd=0, command=home_page).pack()

def deposit_page():
    clear_page()
    main_canvas.yview_moveto(0)
    
    box_wrapper = Frame(content_frame, bg=light)
    box_wrapper.pack(pady=80, expand=True)
    
    box = Frame(box_wrapper, bg=white, bd=3, relief=RIDGE)
    box.pack(ipadx=40, ipady=20)
    
    Label(box, text="Secure Money Deposit", font=("Arial", 26, "bold"), bg=white, fg=navy).pack(pady=20)
    
    Label(box, text="Account Number", font=("Arial", 14), bg=white).pack(anchor="w", padx=60)
    acc_entry = Entry(box, font=("Arial", 14), width=30)
    acc_entry.pack(pady=8, padx=60)
    
    Label(box, text="Amount to Deposit", font=("Arial", 14), bg=white).pack(anchor="w", padx=60)
    amt_entry = Entry(box, font=("Arial", 14), width=30)
    amt_entry.pack(pady=8, padx=60)
    
    def submit():
        acc = acc_entry.get().strip()
        amt_str = amt_entry.get().strip()
        
        try:
            amt = float(amt_str)
            if amt <= 0: raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please input a valid transfer amount")
            return
            
        cursor.execute("SELECT balance FROM accounts WHERE acc_no=?", (acc,))
        row = cursor.fetchone()
        if not row:
            messagebox.showerror("Error", "Target Account Number not found")
            return
            
        new_bal = row[0] + amt
        cursor.execute("UPDATE accounts SET balance=? WHERE acc_no=?", (new_bal, acc))
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO transactions (acc_no, type, amount, date) VALUES (?, 'Deposit', ?, ?)", (acc, amt, now))
        conn.commit()
        
        messagebox.showinfo("Success", f"Successfully Deposited ₹{amt:.2f}.\nUpdated Balance: ₹{new_bal:.2f}")
        home_page()

    Button(box, text="Process Deposit", font=("Arial", 14, "bold"), bg=navy, fg=white, width=20, command=submit).pack(pady=20)
    Button(box, text="← Back to Home", font=("Arial", 12), bg="gray", fg=white, width=15, bd=0, command=home_page).pack()

def withdraw_page():
    clear_page()
    main_canvas.yview_moveto(0)
    
    box_wrapper = Frame(content_frame, bg=light)
    box_wrapper.pack(pady=80, expand=True)
    
    box = Frame(box_wrapper, bg=white, bd=3, relief=RIDGE)
    box.pack(ipadx=40, ipady=20)
    
    Label(box, text="Instant Withdrawal", font=("Arial", 26, "bold"), bg=white, fg=navy).pack(pady=20)
    
    Label(box, text="Account Number", font=("Arial", 14), bg=white).pack(anchor="w", padx=60)
    acc_entry = Entry(box, font=("Arial", 14), width=30)
    acc_entry.pack(pady=8, padx=60)
    
    Label(box, text="Amount to Withdraw", font=("Arial", 14), bg=white).pack(anchor="w", padx=60)
    amt_entry = Entry(box, font=("Arial", 14), width=30)
    amt_entry.pack(pady=8, padx=60)
    
    def submit():
        acc = acc_entry.get().strip()
        amt_str = amt_entry.get().strip()
        
        try:
            amt = float(amt_str)
            if amt <= 0: raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric value")
            return
            
        cursor.execute("SELECT balance FROM accounts WHERE acc_no=?", (acc,))
        row = cursor.fetchone()
        if not row:
            messagebox.showerror("Error", "Target Account Number not found")
            return
            
        if row[0] < amt:
            messagebox.showerror("Error", "Insufficient funds available")
            return
            
        new_bal = row[0] - amt
        cursor.execute("UPDATE accounts SET balance=? WHERE acc_no=?", (new_bal, acc))
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO transactions (acc_no, type, amount, date) VALUES (?, 'Withdrawal', ?, ?)", (acc, amt, now))
        conn.commit()
        
        messagebox.showinfo("Success", f"Successfully Withdrew  ₹{amt:.2f}.\nUpdated Balance:  ₹{new_bal:.2f}")
        home_page()

    Button(box, text="Process Withdrawal", font=("Arial", 14, "bold"), bg=navy, fg=white, width=20, command=submit).pack(pady=20)
    Button(box, text="← Back to Home", font=("Arial", 12), bg="gray", fg=white, width=15, bd=0, command=home_page).pack()

def balance_page():
    clear_page()
    main_canvas.yview_moveto(0)
    
    box_wrapper = Frame(content_frame, bg=light)
    box_wrapper.pack(pady=80, expand=True)
    
    box = Frame(box_wrapper, bg=white, bd=3, relief=RIDGE)
    box.pack(ipadx=40, ipady=20)
    
    Label(box, text="Check Current Balance", font=("Arial", 26, "bold"), bg=white, fg=navy).pack(pady=20)
    
    Label(box, text="Enter Account Number", font=("Arial", 14), bg=white).pack(anchor="w", padx=60)
    acc_entry = Entry(box, font=("Arial", 14), width=30)
    acc_entry.pack(pady=8, padx=60)
    
    output_label = Label(box, text="", font=("Arial", 16, "bold"), bg=white, fg=blue)
    output_label.pack(pady=10)
    
    def inquiry():
        acc = acc_entry.get().strip()
        cursor.execute("SELECT name, balance FROM accounts WHERE acc_no=?", (acc,))
        row = cursor.fetchone()
        if row:
            output_label.config(text=f"Customer Name: {row[0]}\nAvailable Balance:  ₹{row[1]:.2f}", fg="green")
        else:
            output_label.config(text="Account Number Error: Record Not Found", fg="red")

    Button(box, text="Fetch Balance", font=("Arial", 14, "bold"), bg=navy, fg=white, width=20, command=inquiry).pack(pady=15)
    Button(box, text="← Back to Home", font=("Arial", 12), bg="gray", fg=white, width=15, bd=0, command=home_page).pack()

def history_page(mini=False):
    clear_page()
    main_canvas.yview_moveto(0)
    
    box_wrapper = Frame(content_frame, bg=light)
    box_wrapper.pack(pady=50, expand=True, fill=X, padx=100)
    
    title_text = "Recent Mini Statement" if mini else "Full Transaction Log"
    
    box = Frame(box_wrapper, bg=white, bd=3, relief=RIDGE)
    box.pack(fill=X, ipady=20, padx=20)
    
    Label(box, text=title_text, font=("Arial", 26, "bold"), bg=white, fg=navy).pack(pady=20)
    
    search_frame = Frame(box, bg=white)
    search_frame.pack(pady=10)
    
    Label(search_frame, text="Account Number: ", font=("Arial", 14), bg=white).pack(side=LEFT, padx=5)
    acc_entry = Entry(search_frame, font=("Arial", 14), width=15)
    acc_entry.pack(side=LEFT, padx=5)
    
    # Simple table display element
    table_frame = Frame(box, bg=white)
    table_frame.pack(pady=15, fill=X, padx=40)
    
    def load_records():
        for widget in table_frame.winfo_children():
            widget.destroy()
            
        acc = acc_entry.get().strip()
        if mini:
            cursor.execute("SELECT type, amount, date FROM transactions WHERE acc_no=? ORDER BY id DESC LIMIT 5", (acc,))
        else:
            cursor.execute("SELECT type, amount, date FROM transactions WHERE acc_no=? ORDER BY id DESC", (acc,))
            
        rows = cursor.fetchall()
        
        if not rows:
            Label(table_frame, text="No transactions recorded for this account.", font=("Arial", 12, "italic"), bg=white, fg="gray").pack()
            return
            
        # Table Headers
        headers = ["Type", "Amount", "Timestamp"]
        for col_idx, text in enumerate(headers):
            Label(table_frame, text=text, font=("Arial", 12, "bold"), bg="#EAF2FF", relief=RIDGE, width=20).grid(row=0, column=col_idx, sticky="nsew")
            
        for row_idx, row in enumerate(rows, start=1):
            bg_color = "white" if row_idx % 2 == 0 else "#F9FAFC"
            for col_idx, val in enumerate(row):
                val_text = f" ₹{val:.2f}" if isinstance(val, float) else str(val)
                Label(table_frame, text=val_text, font=("Arial", 11), bg=bg_color, relief=RIDGE, width=20).grid(row=row_idx, column=col_idx, sticky="nsew")

    Button(search_frame, text="Load Logs", font=("Arial", 11, "bold"), bg=blue, fg=white, command=load_records).pack(side=LEFT, padx=10)
    Button(box, text="← Back to Home", font=("Arial", 12), bg="gray", fg=white, width=15, bd=0, command=home_page).pack(pady=10)

# ================= HOME PAGE =================

def home_page():
    clear_page()
    global slider_label

    main_canvas.yview_moveto(0)

    # ===== TOP SECTION =====
    top = Frame(content_frame, bg=blue)
    top.pack(fill=X, ipady=5)

    top.grid_columnconfigure(0, weight=1)
    top.grid_columnconfigure(1, weight=1)

    left = Frame(top, bg=blue)
    left.grid(row=0, column=0, sticky="w", padx=50, pady=10)

    Label(
        left,
        text="Welcome to Royal Trust Bank",
        font=("Arial", 36, "bold"),
        bg=blue,
        fg=white
    ).pack(anchor="w")

    slider_label = Label(
        left,
        text="",
        font=("Arial", 18),
        bg=blue,
        fg="#DDEEFF"
    )
    slider_label.pack(anchor="w", pady=10)

    Button(
        left,
        text="Login",
        font=("Arial", 14, "bold"),
        bg=gold,
        fg="black",
        padx=20,
        pady=6,
        bd=0,
        command=login_page
    ).pack(anchor="w")

    # ===== BANK EMOJI =====
    Label(
        top,
        text="🏦",
        font=("Arial", 100),
        bg=blue,
        fg=white
    ).grid(row=0, column=1, sticky="e", padx=50)

    # ===== SERVICES TITLE =====
    Label(
        content_frame,
        text="Our Banking Services",
        font=("Arial", 28, "bold"),
        bg=light,
        fg=navy
    ).pack(pady=15)

    # ===== CARDS FRAME =====
    cards = Frame(content_frame, bg=light)
    cards.pack(pady=5)

    # ===== CARD ROUTING INTERFACE FUNCTION =====
    def create_card(symbol, title, text, row, column, command):
        card = Frame(
            cards,
            bg=white,
            width=280,      
            height=250,     
            bd=2,
            relief=RIDGE,
            cursor="hand2"
        )
        card.grid(row=row, column=column, padx=25, pady=10)
        card.pack_propagate(False)

        Label(
            card,
            text=symbol,
            font=("Arial", 45),
            bg=white
        ).pack(pady=10)

        Label(
            card,
            text=title,
            font=("Arial", 16, "bold"),
            bg=white,
            fg=navy
        ).pack()

        Label(
            card,
            text=text,
            font=("Arial", 12),
            bg=white,
            fg="gray"
        ).pack(pady=5)

        Button(
            card,
            text="Open",
            font=("Arial", 12, "bold"),
            bg=navy,
            fg=white,
            bd=0,
            padx=20,
            pady=6,
            cursor="hand2",
            command=command
        ).pack(side=BOTTOM, pady=15)

    # ===== FIRST ROW (Mapped cleanly to distinct menus) =====
    create_card("💳", "Create Account", "Open secure account", 0, 0, create_account_page)
    create_card("💰", "Deposit", "Deposit money safely", 0, 1, deposit_page)
    create_card("💸", "Withdraw", "Withdraw instantly", 0, 2, withdraw_page)

    # ===== SECOND ROW =====
    create_card("📊", "Balance", "Check current balance", 1, 0, balance_page)
    create_card("📜", "Transactions", "View transaction history", 1, 1, lambda: history_page(mini=False))
    create_card("🧾", "Mini Statement", "Recent account activity", 1, 2, lambda: history_page(mini=True))

    start_slider()

# ================= NAVBAR BUTTONS =================

menu = Frame(navbar, bg=navy)
menu.pack(side=RIGHT, padx=20)

buttons = [
    ("Home", home_page),
    ("About", about_page),
    ("Contact", contact_page),
    ("Login", login_page)
]

for text, cmd in buttons:
    Button(
        menu,
        text=text,
        font=("Arial", 14, "bold"),
        bg=navy,
        fg=white,
        bd=0,
        padx=15,
        command=cmd
    ).pack(side=LEFT, padx=10)

# ================= START =================

home_page()
root.mainloop()
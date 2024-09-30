import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
root = tk.Tk()
root.geometry("400x400")
root.configure(bg="#A9A9A9")
root.title("Login")
def login():
    username = username_entry.get()
    password = password_entry.get()
    if not username or not password:
        messagebox.showerror("Error", "Please fill all fields")
        return
    conn = sqlite3.connect('uu.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()
    conn.close()
    if result:
        messagebox.showinfo("Success", "Login successful!")
        root.destroy()  
        next_page = tk.Tk()
        next_page.geometry("400x500") 
        next_page.configure(bg="#8B8878")
        next_page.title("Student Registration!")
        welcome_label = tk.Label(next_page, text=f"Welcome to Information Technology Student, {username}!")
        welcome_label.pack()
        next_page.mainloop()  
    else:
        messagebox.showerror("Error", "Invalid username or password")
login_page_label=tk.Label(root,text="Login Page",bg="#A9A9A9",fg="#ffffff",font=("Arial",17),pady=17)
login_page_label.grid(row=0,column=0,columnspan=10)
username_label = tk.Label(root, text="Username:",bg="#A9A9A9", font=("Arial", 12),pady=13)
username_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
username_entry = tk.Entry(root,font=("Arial", 14))
username_entry.grid(row=1, column=1, padx=10, pady=10)
password_label = tk.Label(root, text="Password:",bg="#A9A9A9", font=("Arial", 12))
password_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
password_entry = tk.Entry(root,font=("Arial", 14), show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)
# Create the login button
login_button = ttk.Button(root, text="Login", command=login, width=10)
login_button.grid(row=3, column=1, columnspan=1, padx=10, pady=10)
cancel_button = ttk.Button(root, text="Cancel", command=login, width=10)
cancel_button.grid(row=3, column=2)
root.mainloop() 
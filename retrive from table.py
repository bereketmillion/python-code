from tkinter import ttk
import tkinter as tk
import sqlite3
def View():
    con1 = sqlite3.connect("uu.db")
    cur1 = con1.cursor()
    cur1.execute("SELECT * FROM student")
    rows = cur1.fetchall()    
    for row in rows:
        print(row) 
        tree.insert("", tk.END, values=row)        
    con1.close() 
root = tk.Tk()
tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4", "c5"), show='headings')
tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="firstname")
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="secondname")
tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="idno")
tree.column("#4", anchor=tk.CENTER)
tree.heading("#4", text="department")
tree.column("#5", anchor=tk.CENTER)
tree.heading("#5", text="year")
tree.pack()
button1 = tk.Button(text="Display data", command=View)
button1.pack(pady=10)
root.mainloop()
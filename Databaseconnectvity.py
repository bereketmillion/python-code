import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
top = tk.Tk()
top.title("registration")
top.geometry("400x500")
top.configure(bg="#8B8878")
frame=tk.Frame(bg="#8B8878")
def insert_data():
    firstname = first_entry.get()
    secondname = second_entry.get()
    idno=idno_entry.get()
    department=dept_entry.get()
    year=year_entry.get()
    username=username_entry.get()
    password=pass_entry.get()
    if not firstname or not secondname:
        messagebox.showerror("Error", "Please fill all fields")
        return
    elif not idno or not department:
        messagebox.showerror("Error", "Please fill all fields")
        return
    elif not year or not password:
        messagebox.showerror("Error", "Please fill all fields")
        return
    try:
        year = int(year)
    except ValueError:
        messagebox.showerror("Error", "year must be a number")
        return
    conn = sqlite3.connect('uu.db')
    cursor = conn.cursor() #database pointer
#    cursor.execute("CREATE TABLE student(firstname Text Not NULL,secondname Text Not NULL, idno text primary key Not NULL,department Text Not NULL,year integer Not NULL,username Text Not NULL,password Text Not NULL)")
    cursor.execute("INSERT INTO student (firstname,secondname,idno,department,year,username,password ) VALUES (?, ?,?,?,?,?,?)", (firstname,secondname,idno,department,year,username,password))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Data inserted successfully!")
def search_data():
        idno = idno_entry.get()
        if not idno:
            messagebox.showerror("Error", "Please enter Idno")
            return
        conn = sqlite3.connect('uu.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student WHERE idno = ?", (idno,))
        result = cursor.fetchone() #fetchone:retrive only single row
        conn.close()
        if result:
            first_entry.insert(0, result[0])
            second_entry.insert(0, result[1])
            dept_entry.insert(0, result[3])
            year_entry.insert(0, result[4])
            username_entry.insert(0, result[5])
            pass_entry.insert(0, result[6])
            messagebox.showinfo("Found", "Data found")
        else:
            messagebox.showinfo("Not Found", "No data found")
def clear_input():
    first_entry.delete(0,tk.END)
    second_entry.delete(0,tk.END)
    idno_entry.delete(0,tk.END)
    dept_entry.delete(0,tk.END)
    year_entry.delete(0,tk.END)
    username_entry.delete(0,tk.END)
    pass_entry.delete(0, tk.END)
def delete_data():
    idno = idno_entry.get()
    if not idno:
        messagebox.showerror("Error", "Please enter idno")
        return
    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this data?"):
        conn = sqlite3.connect('uu.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM student WHERE idno = ?", (idno,))
        conn.commit()
        conn.close()
        clear_input()
        messagebox.showinfo("Success", "Data deleted successfully!")
def update_data():
    firstname = first_entry.get()
    secondname = second_entry.get()
    idno=idno_entry.get()
    department=dept_entry.get()
    year=year_entry.get()
    username=username_entry.get()
    password=pass_entry.get()
    if not firstname or not secondname:
        messagebox.showerror("error","fill all data")
        return
    elif not year or not department:
      messagebox.showerror("error","fill all data")
    try:
        year = int(year)
    except ValueError:
        messagebox.showerror("Error", "year must be a number")
        return
    conn = sqlite3.connect('uu.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE student SET firstname = ?,secondname=?,department=?,year=?,username=?,password=? WHERE idno = ?", (firstname,secondname,idno,department,year,username,password))
    conn.commit()
    conn.close()

username_entry.grid(row=6,column=1)
pass_label.grid(row=7,column=0)
pass_entry.grid(row=7,column=1)
insert_button.grid(row=8,column=1,padx=13)
retrive_button.grid(row=8,column=2,padx=5)
search_button.grid(row=8,column=3,padx=13)
update_button.grid(row=8,column=4,padx=13)
delete_button.grid(row=8,column=5,padx=13)
clear_button.grid(row=8,column=6,pady=13) messagebox.showinfo("Success", "Data updated successfully!")
Registration_label=tk.Label(frame,text="Registration",bg="#8B8878",fg="#ffffff",font=("Arial",20),pady=20)
Registration_label.grid(row=0,column=0,columnspan=10)
Fisrt_label=tk.Label(frame,text="FirstName",bg="#8B8878",fg="#ffffff",font=("Arial",14),pady=13)
first_entry=tk.Entry(frame,font=("Arial",12))
second_label=tk.Label(frame,text="SecondName",bg="#8B8878",fg="#ffffff",font=("Arial",14),pady=13)
second_entry=tk.Entry(frame,font=("Arial",12))
idno_label=tk.Label(frame,text="Idno",bg="#8B8878",fg="#ffffff",font=("Arial",14),pady=13)
idno_entry=tk.Entry(frame,font=("Arial",12))
dept_label=tk.Label(frame,text="Department",bg="#8B8878",fg="#ffffff",font=("Arial",14),pady=13)
dept_entry=tk.Entry(frame,font=("Arial",12))
year_label=tk.Label(frame,text="Year",bg="#8B8878",fg="#ffffff",font=("Arial",14),pady=13)
year_entry=tk.Entry(frame,font=("Arial",12))
pass_label=tk.Label(frame,text="Password",bg="#8B8878",fg="#ffffff",font=("Arial",14),pady=13)
pass_entry=tk.Entry(frame,show="*",font=("Arial",12),fg="#ff3399")
username_label=tk.Label(frame,text="Username",bg="#8B8878",fg="#ffffff",font=("Arial",14),pady=13)
username_entry=tk.Entry(frame,font=("Arial",12),fg="#ff3399")
insert_button=tk.Button(frame,text="Insert",fg="#ff3399",command=insert_data,font=("Arial",14))
retrive_button=tk.Button(frame,text="Retrive",fg="#ff3399",font=("Arial",14))
search_button=tk.Button(frame,text="Search",fg="#ff3399",command=search_data,font=("Arial",14))
delete_button=tk.Button(frame,text="Delete",command=delete_data,fg="#ff3399",font=("Arial",14))
update_button=tk.Button(frame,text="Update",command=update_data,fg="#ff3399",font=("Arial",14))
clear_button=tk.Button(frame,text="Clear",fg="#ff3399",command=clear_input,font=("Arial",14))
Fisrtd_label.grid(row=1,column=0)
first_entry.grid(row=1,column=1)
second_label.grid(row=2,column=0)
second_entry.grid(row=2,column=1)
idno_label.grid(row=3,column=0)
idno_entry.grid(row=3,column=1)
dept_label.grid(row=4,column=0)
dept_entry.grid(row=4,column=1)
year_label.grid(row=5,column=0)
year_entry.grid(row=5,column=1)
username_label.grid(row=6,column=0)
frame.pack()
top.mainloop()
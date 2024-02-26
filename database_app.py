import tkinter as tk
import sqlite3

def create_table():
    # Connect to the database (creates if not exists)
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    
    # Create a table
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

def insert_data(name, email):
    # Connect to the database
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    
    # Insert data into the table
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

def main():
    # Create the GUI
    root = tk.Tk()
    root.title("Database Example")
    
    # Create the database table if it doesn't exist
    create_table()
    
    # Function to handle button click
    def add_user():
        name = name_entry.get()
        email = email_entry.get()
        insert_data(name, email)
        status_label.config(text="User added successfully.")
    
    # Entry fields
    tk.Label(root, text="Name:").pack()
    name_entry = tk.Entry(root)
    name_entry.pack()
    
    tk.Label(root, text="Email:").pack()
    email_entry = tk.Entry(root)
    email_entry.pack()
    
    # Button to add user
    add_button = tk.Button(root, text="Add User", command=add_user)
    add_button.pack()
    
    # Status label
    status_label = tk.Label(root, text="")
    status_label.pack()
    
    root.mainloop()

if __name__ == "__main__":
    main()

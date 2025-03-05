import sqlite3
import tkinter as tk
from tkinter import ttk, font, messagebox, PhotoImage

#creating a database
conn = sqlite3.connect('task.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL)""")

conn.commit()

#creating a window
window = tk.Tk()
window.title("To-Do List")
window.configure(bg="#f0f0f0")
window.geometry("500x600")

#UI elements
header_font = font.Font(family="Garamond", size=24, weight="bold")
header_label = tk.Label(window, text="To-Do List", font=header_font, bg="#f0f0f0", fg="#333")

window.mainloop()
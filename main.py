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
header_label.pack(pady=20)

frame = tk.Frame(window, bg="#f0f0f0")
frame.pack(pady=10)

task_entry = tk.Entry(frame, font=("Garamond", 16),bg='white',fg='grey')
task_entry.insert(0, "Enter a task...")
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", font=("Garamond", 14), bg="#4CAF50", fg="#fff")  
# command=lambda: add_task()
add_button.pack(side=tk.LEFT,pady=10)

task_list_frame = tk.Frame(window, bg='white')
task_list_frame.pack(fill=tk.BOTH, expand=True)

task_listbox = tk.Listbox(window, font=("Garamond", 14), bg="#fff", fg="#333", selectmode=tk.SINGLE)

canvas = tk.Canvas(task_list_frame, bg='white')
canvas.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)
window.mainloop()
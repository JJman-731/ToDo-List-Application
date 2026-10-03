import json
import tkinter as tk
from tkinter import simpledialog

FILENAME = "tasks.json"
tasks = []


def load_tasks():
    global tasks
    try:
        with open(FILENAME, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []


def save_tasks():
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)


def refresh_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        prefix = "[x] " if task["done"] else "[ ] "
        listbox.insert(tk.END, prefix + task["description"])


def add_task():
    description = simpledialog.askstring("New Task", "Task description:")
    if description:
        tasks.append({"description": description, "done": False})
        save_tasks()
        refresh_listbox()


def complete_task():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        tasks[index]["done"] = True
        save_tasks()
        refresh_listbox()


def remove_task():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        tasks.pop(index)
        save_tasks()
        refresh_listbox()


load_tasks()

root = tk.Tk()
root.title("To-Do List")
root.geometry("300x350")

listbox = tk.Listbox(root, width=65, height=25)
listbox.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Add", command=add_task).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Complete", command=complete_task).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Remove", command=remove_task).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Quit", command=root.quit).grid(row=0, column=3, padx=5)

refresh_listbox()
root.mainloop()
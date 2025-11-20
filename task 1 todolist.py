import tkinter as tk
root = tk.Tk()
root.title("To-Do List")
root.geometry("350x400")
tasks = []
def update_listbox():
    listbox.delete(0, tk.END)
    for t in tasks:
        listbox.insert(tk.END, t)
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        entry.delete(0, tk.END)
        update_listbox()
def delete_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_listbox()
def update_task():
    selected = listbox.curselection()
    if selected:
        tasks[selected[0]] = entry.get()
        entry.delete(0, tk.END)
        update_listbox()
listbox = tk.Listbox(root, width=40, height=15)
listbox.pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack()
tk.Button(root, text="Add Task", width=20, command=add_task).pack(pady=5)
tk.Button(root, text="Update Task", width=20, command=update_task).pack(pady=5)
tk.Button(root, text="Delete Task", width=20, command=delete_task).pack(pady=5)
root.mainloop()

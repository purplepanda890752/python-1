import tkinter as tk
from tkinter import messagebox

def show_info():
    name = name_entry.get()
    activity = activity_entry.get()
    color = color_entry.get()
    checked = "Yes" if tick_var.get() else "No"

root = tk.Tk()
root.title("My Info")
root.configure(bg="light blue")

tk.Label(root, text ="Your Name:", bg="light blue").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Favorite Activity:", bg="light blue").pack()
activity_entry = tk.Entry(root)
activity_entry.pack()

tk.Label(root, text="Favorite Color:", bg="light blue").pack()
color_entry = tk.Entry(root)
color_entry.pack()

tick_var = tk.BooleanVar()
tk.Checkbutton(root, text="Tick this box", variable=tick_var, bg="light blue").pack()

tk.Button(root, text="Show Info", command=show_info).pack()

root.mainloop()
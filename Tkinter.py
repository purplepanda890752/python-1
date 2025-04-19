import tkinter as tk

root = tk.Tk()
root.title("Black Background Window")
root.configure(bg="black")
root.geometry("400x300")

label = tk.Label(root, text="Hello, Tkinter!", bg="black", fg="white", font=("Arial", 20))
label.pack(expand=True, fill="both")

root.mainloop()         

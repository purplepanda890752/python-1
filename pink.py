import tkinter as tk

root = tk.Tk()
root.title("Tick Box Example")
root.configure(bg="pink")

var = tk.IntVar()

checkbox = tk.Checkbutton(root, text="Tick me!", variable=var, bg="pink")
checkbox.pack(pady=20)

root.mainloop()
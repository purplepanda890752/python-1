#Import neccesary libary 
from tiker import*

#create window
root=tk()
root.title('log in app')
root.geometry("'400x400")

#create a frame to organize elements better
frame=frame(master=root, height=200,width=360, bg='d0efff')
#add widgets
#add labels
Ib11= Label(frame,text=" Full name", bg="#3895d3",fg='white'
width=12)
Ib11= Label(frame,text=" Full name", bg="#3895d3",fg='white'
width=12)
Ib11= Label(frame,text=" Full name", bg="#3895d3",fg='white'
width=12)
#use entry widget to create a text box for users to enter details
name_entry= Entry(frame)
name_entry= Entry(frame)
name_entry= Entry(frame)
#function to display message
def display():
    # Import necessary libraries
from tkinter import *

# Create Window
root = Tk()
root.title('Number Pad')
root.geometry('250x300')

# Create a frame to organize elements better
# frame = Frame(master=root, height=200, width=360, bg='blue')
nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ['#', 0, '*']]

for i in range(4):

    # Configure rows and columns to resize window
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 3):
        frame = Frame(
            master=root,
            relief=SUNKEN,
            borderwidth=1
        )

    
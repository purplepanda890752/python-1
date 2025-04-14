# import neccesary libraries
from Tkinter import*
Window= Tk()

#set the window Title and geometry
Window.title('Demo window')
Window.geoemtry('400x300')
#Import necessary
from Tkinter import*
from datetime import date

#create window
root= Tk()
root.title('Getting started with widgets')
root.geoemtry('400x300')

#Add widgets
#Add labels
Ibl= label(text="Hey there!", fg=:"White", bg="#072F5F"
height=1,width=300)

#Add label for getting name as input from user
#Use entry Widget to create a text box for user to enter details
name_label= Label(text="Full name", bg="#389SD3")
name_entry= Entry()

def display():
    #Read input given by user
    name= name_entry.get()

    Declaring a global variable
    # to make it accesibile anywhere in the program
    global message
    message="Welcome to the application!/n Todays date is" \
      greet = "Hello "+name+"\n"

    # Display details in a text box
    # Specify where to add the details inside the text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

# Add a Text Widget to display information/messages
text_box = Text(height=3)

# Add button and give value of command as name of the function
# Press button, display function will be called automatically
btn = Button(text="Begin", command=display, height=1,
             bg="#1261A0", fg='white')

# Organize all the widgets in the window
btn.pack()
# Add a Text Widget to display information/messages
text_box = Text(height=3)

# Add button and give value of command as name of the function
# Press button, display function will be called automatically
btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg='white')

# Organize all the widgets in the window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

#page to be shown after logging in successfully
#page name - user

from gc import disable
from threading import local
from tkinter import *
import os
from turtle import width
import mysql.connector
from essential import *

# Create a connection to the database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port = 3307,
    database="test",
)

# Create a cursor
cursor = connection.cursor()

root = Tk()
root.geometry("1250x768")

title_bar(root,"ABC BUILDERS")

#main frame
f1= Frame(root)
f1.configure(bg="#222222")
f1.pack(side=TOP, expand = True, fill="both")

#annoucement frame
f2= Frame(f1)
f2.configure(bg="gold")
f2.pack(side=RIGHT, fill=Y)
f2.configure(width=390)


heading1 = Label(f1,text="WELCOME ________hjfjdgjdgjdj__", font=("Roboto", 32, "bold"),fg="gold",bg="#222222")
heading1.place(relx=0.35,rely=0.20,anchor='center')


#various operations
def Edit_Your_Profile():
    pass

def Pay_Maintanence():
    pass

def Announcement_To_Community():
    pass

def View_Our_Community_Strength():
    pass

#########################################################################
def Images_for_announcements():
    f4 = Frame(f1)
    f4.configure(bg="#111111")
    f4.place(relx=0.1,rely=0.1,relheight=0.8,relwidth=0.8)

    def exit():
        f4.destroy()

    Close_button = Button(f4)
    Close_button.configure(text="X")
    Close_button.configure(bg="red")
    Close_button.configure(activebackground="blue")
    Close_button.configure(command=exit)
    Close_button.place(relx=0.983,rely=0)
#########################################################################

#buttons for various operations
button1 = Button(f1)
button1.configure(text="=> Edit Your Profile")
button1.configure(font=("Roboto", 24, "bold"))
button1.configure(fg="gold",bg="#111111")
button1.configure(activebackground="gold")
button1.configure(command=Edit_Your_Profile)
button1.place(relx=0.1,rely=0.3)

button2 = Button(f1)
button2.configure(text="=> Pay Maintanance")
button2.configure(font=("Roboto", 24, "bold"))
button2.configure(fg="gold",bg="#111111")
button2 .configure(activebackground="gold")
button2.configure(command=Pay_Maintanence)
button2.place(relx=0.1,rely=0.4)

button3 = Button(f1)
button3.configure(text="=> Announcement To Community")
button3.configure(font=("Roboto", 24, "bold"))
button3.configure(fg="gold",bg="#111111")
button3 .configure(activebackground="gold")
button3.configure(command=Announcement_To_Community)
button3.place(relx=0.1,rely=0.5)

button4 = Button(f1)
button4.configure(text="=> View Our Community Strength")
button4.configure(font=("Roboto", 24, "bold"))
button4.configure(fg="gold",bg="#111111")
button4 .configure(activebackground="gold")
button4.configure(command=View_Our_Community_Strength)
button4.place(relx=0.1,rely=0.6)


#content in annoucement frame
heading2 = Label(f2,text="Announcement", font=("Roboto", 16, "bold"),fg="gold",bg="#222222")
heading2.place(relx=0.25,rely=0.2,anchor='center')


def carousel(announcements):
    f3= Frame(f2)
    content = Text(f3)
    content.pack()
    announcement=announcements
    scrollbar = Scrollbar(f3, command=content.yview)
    content.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    v=announcement[0]
    content.insert("1.0",v)
    
    i=0
    def right():
        nonlocal i
        content.configure(state="normal")
        content.delete("1.0","end")
        i=(i+1)%(len(announcement))
        text=announcement[i]
        content.insert("1.0",text)
        content.configure(state="disabled")

    def left():
        nonlocal i
        content.configure(state="normal")
        content.delete("1.0","end")
        i=(i-1)%(len(announcement))
        text=announcement[i]
        content.insert("1.0",text)
        content.configure(state="disabled")
    
    # content.insert("1.0",[0])
    

#left button
    right_but = Button(f2, text=">")
    right_but.configure(fg="#222222",bg="gold")
    right_but.configure(command=right)
    right_but.place(relx=0.9 ,rely=0.5)

#right button
    left_but = Button(f2, text="<")
    left_but.configure(fg="#222222",bg="gold")
    left_but.configure(command=left)
    left_but.place(relx=0.05 ,rely=0.5)
    
    content.config(state=DISABLED)
    
    f3.place(relx=0.1, rely=0.27, relheight=0.5, relwidth=0.8)

###############################################################################################
    button5 = Button(f3)
    button5.configure(text="Images attached")
    button5.configure(font=("Roboto", 10, "bold"))
    button5.configure(fg="gold",bg="#111111")
    button5 .configure(activebackground="gold")
    button5.configure(command=Images_for_announcements)
    button5.place(relx=0.35,rely=0.92)
################################################################################################

announcements = ["This is the first announcement.", "This is the second announcement.", "This is the third announcement.", "This is the fourth announcement."]
carousel(announcements)


# Close the cursor and connection
cursor.close()
connection.close()


root.mainloop()



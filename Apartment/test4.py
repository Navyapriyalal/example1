#page to be shown after pressing pay button in maintenance_records (create a button in maintenance_records file for this)
#****there should be no menu bar inside this page****
#page name - pay_maintenance

from essential import *
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector


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

#main frame
f1= Frame(root)
f1.configure(bg="#222222")
f1.pack(side=TOP, expand = True, fill="both")



#content under due payment frame
maintenance = Label(f1)
maintenance.configure(text="PAYMENT", font=("Roboto", 24, "bold"),fg="#FFD700",bg="#222222")
maintenance.place(relx=0.45, rely=0.25)

text1 = Label(f1,text="Accept to pay maintenance", font=("Roboto", 12, "bold"),fg="#FFD700",bg="#222222")
text1.place(relx=0.65,rely=0.64)

text2 = Label(f1,text="Decline to go back to \nmaintenance payment page", font=("Roboto", 12, "bold"),fg="#FFD700",bg="#222222")
text2.place(relx=0.20,rely=0.64)

def decline(self):
    pass

def accept(self):
    pass

Decline = Button(f1)
Decline.pack()
Decline.place(relx= 0.25, rely=0.7)
Decline.configure(text="Decline",height=3, width=10, bg="gold", fg="black")
Decline.configure(command=decline)
Decline.configure(activebackground="gold")
Decline.configure(cursor="hand2")

Accept = Button(f1)
Accept.pack()
Accept.place(relx=0.70, rely=0.7)
Accept.configure(text="Accept",height=3, width=10, bg="gold", fg="black")
Accept.configure(command=accept)
Accept.configure(activebackground="gold")
Accept.configure(cursor="hand2")




cursor.close()
connection.close()


root.mainloop()
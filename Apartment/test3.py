#page to be shown after pressing pay maintenance
#page name - maintenance_records

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

#due payment frame
f2 = Frame(f1)
f2.configure(bg="#333333")
f2.place(relx=0.0, rely=0.2, relwidth=0.5, relheight=1)

#paid payment frame
f3 = Frame(f1)
f3.configure(bg="#111111")
f3.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=1)

def switch_pay_maintenance():
    pass

#pay button
button1 = Button(f2)
button1.configure(text="Pay")
button1.configure(font=("Roboto", 24, "bold"))
button1.configure(fg="gold",bg="#111111")
button1.configure(activebackground="gold")
button1.configure(command=switch_pay_maintenance)
button1.place(relx=0.1,rely=0.3)


#content under due payment frame
due = Label(f2)
due.configure(text="DUE", font=("Roboto", 24, "bold"),fg="#FFD700",bg="#333333")
due.place(relx=0.4, rely=0.05)


#content under paid payment frame
paid = Label(f3)
paid.configure(text="PAID", font=("Roboto", 24, "bold"),fg="#FFD700",bg="#111111")
paid.place(relx=0.45, rely=0.05)

cursor.close()
connection.close()


root.mainloop()
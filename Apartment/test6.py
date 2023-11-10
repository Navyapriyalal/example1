#page to be shown after pressing show cmmunity strength button in user page
#page name - community_strength

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

#container frame
f1= Frame(root)
f1.pack(side=TOP, expand = True, fill="both")

#create a canvas
my_canvas= Canvas(f1)
my_canvas.pack(side=LEFT, fill="both", expand= True)

#add a scrollbar to canvas
# scrollbar = Scrollbar(f1, orient=VERTICAL, command=my_canvas.yview)
# scrollbar.pack(side=RIGHT, fill='y')

# #configure canvas
# my_canvas.configure(yscrollcommand=scrollbar.set)
# my_canvas.bind('<Configure>', lambda e : my_canvas.configure(scrollregion= my_canvas.bbox("all")))

#main frame
f2= Frame()
f2.configure(bg="#222222")

#adding main frame to canvas window
my_canvas.create_window((0,0), window=f2, anchor='nw', width=root.winfo_screenwidth(), height=10000)

# for i in range(100):
#     Button(f2, text=f'Button {i}').grid(row=i, column=0, pady=10, padx=10)

# frame_rely = 0.1

#title
Label(f2, bg = "#222222").grid(row=1,pady=30)
Label(f2, bg = "#111111").grid(row=2)
Label(f2, bg = "#444444").grid(row=3)
Label(f2, bg = "#111111").grid(row=4)
Label(f2, bg = "#333333").grid(row=5)
title= Label(f2)
title.configure(text="COMMUNITY STRENGTH", font=("Roboto", 24, "bold"),fg="#FFD700",bg="#222222")
title.grid(row=3)

# for i in range(3):
#     frames = "f"+str(i+3)
#     print(frames)
#     frame_rely= frame_rely+0.25
#     frames = Frame(f2)
#     frames.configure(bg="#333333")
#     frames.place(relx=0.15, rely=frame_rely, relwidth=0.7, relheight=0.2)

#     #content under name frame
#     name = Label(frames)
#     name.configure(text="Name :", font=("Roboto", 16, "bold"),fg="#FFD700",bg="#333333")
#     name.place(relx=0.1, rely=0.1)


#     #content under house frame
#     house_no = Label(frames)
#     house_no.configure(text="House no. :", font=("Roboto", 16, "bold"),fg="#FFD700",bg="#333333")
#     house_no.place(relx=0.1, rely=0.4)

#     #content under date of joining frame
#     date_join = Label(frames)
#     date_join.configure(text="Date of Joining :", font=("Roboto", 16, "bold"),fg="#FFD700",bg="#333333")
#     date_join.place(relx=0.1, rely=0.7)

cursor.close()
connection.close()

root.mainloop()




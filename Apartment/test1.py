#PROFILE PAGE

from tkinter import *
import os
import mysql.connector
from tkinter import filedialog
from PIL import Image, ImageTk
from tkcalendar import Calendar

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

f1= Frame(root)
f1.configure(bg="#222222")
f1.pack(side=TOP, expand = True, fill="both")

heading = Label(f1,text="Your Profile", font=("Roboto", 32, "bold"),fg="#FFD700",bg="#222222")
heading.place(relx=0.42,rely=0.20)

#frame containing the labels and entry widgets
f2 = Frame(f1,height=550,width=1010)
f2.place(relx=0.1,rely=0.3,relheight=0.6,relwidth=0.8)
f2.configure(bg="#111111")

#frame for containing profile pic
f3 = Frame(f2)
f3.place(relx=0.05,rely=0.1,relheight=0.5, relwidth=0.2)
f3.configure(bg="#222222")


#creating labels for profile details
name = Label(f2,text="Name :", font=("Roboto", 16, "bold"),fg="#FFD700",bg="#222222")
name.place(relx=0.4,rely=0.05)
houseno = Label(f2,text="House no. :", font=("Roboto", 16, "bold"),fg="#FFD700",bg="#222222")
houseno.place(relx=0.4,rely=0.15)
blockno = Label(f2,text="Block no. :", font=("Roboto", 16, "bold"),fg="#FFD700",bg="#222222")
blockno.place(relx=0.4,rely=0.25)
username = Label(f2,text="Username :", font=("Roboto", 16, "bold"),fg="#FFD700",bg="#222222")
username.place(relx=0.4,rely=0.35)
password = Label(f2,text="Password :", font=("Roboto", 16, "bold"),fg="#FFD700",bg="#222222")
password.place(relx=0.4,rely=0.45)
phone = Label(f2,text="Phone no. :", font=("Roboto", 16, "bold"),fg="#FFD700",bg="#222222")
phone.place(relx=0.4,rely=0.55)
join_date = Label(f2,text="Date of Joining :", font=("Roboto", 16, "bold"),fg="#FFD700",bg="#222222")###########
join_date.place(relx=0.4,rely=0.65)############
profile = Label(f2,text="Profile Photo", font=("Roboto", 16, "bold"),fg="#FFD700",bg="#222222")
profile.place(relx=0.075,rely=0.7)





#function to upload profile pic
def upload_profile_picture():
    # Open a dialog box that allows the user to select a file from their computer.
    file_path = filedialog.askopenfilename(filetypes=[('Image files', '*.png')])

    # If the user selected a file, load the image and display it in the label.
    if file_path:
        image_obj = Image.open(file_path)
        resize_image = image_obj.resize((250,250))
        img= ImageTk.PhotoImage(resize_image)
    #creating a label to display the profile picture.
        profile_picture_label = Label(f3)
        profile_picture_label.image = img
        profile_picture_label['image']=img
    #profile_picture_label.config()
        profile_picture_label.place(relx=0.0,rely=0.0, relheight=1, relwidth=1)


#creating upload button to upload profile pic
upload_button1 = Button(f3, text="+", command=upload_profile_picture)
upload_button1.place(relx=0.45,rely=0.45)
upload_button1.configure(fg="gold",bg="#111111")


#creating the variables to store the values
name_var = StringVar()
houseno_var = StringVar()
blockno_var = StringVar()
username_var = StringVar()
password_var = StringVar()
phone_var = IntVar()

#calender frame and contents
cal_frame = Frame(root)
cal_frame.place_forget()  # Initially hide the calendar frame

cal = Calendar(cal_frame)
cal.pack(pady=10)

def get_selected_date():
    selected_date = cal.get_date()
    date_entry.delete(0, END)
    date_entry.insert(0, selected_date)
    cal_frame.place_forget()  # Hide the calendar frame
def open_calendar():
    cal_frame.place(relx=0.5, rely=0.5, anchor=CENTER)


#creating entry widgets
name_entry = Entry(f2,textvariable=name_var,font=("Verdana",12 ,"bold"),fg="#FFD700",bg="#111111")
name_entry.place(relx=0.6,rely=0.05,height=30,width=350)
houseno_entry = Entry(f2,textvariable=houseno_var,font=("Verdana",12 ,"bold"),fg="#FFD700",bg="#111111")
houseno_entry.place(relx=0.6,rely=0.15,height=30,width=350)
blockno_entry = Entry(f2,textvariable=blockno_var,font=("Verdana",12 ,"bold"),fg="#FFD700",bg="#111111")
blockno_entry.place(relx=0.6,rely=0.25,height=30,width=350)
username_entry = Entry(f2,textvariable=username_var,font=("Verdana",12 ,"bold"),fg="#FFD700",bg="#111111")
username_entry.place(relx=0.6,rely=0.35,height=30,width=350)
password_entry = Entry(f2,textvariable=password_var,font=("Verdana",12 ,"bold"),fg="#FFD700",bg="#111111")
password_entry.place(relx=0.6,rely=0.45,height=30,width=350)
phone_entry = Entry(f2,textvariable=phone_var,font=("Verdana",12 ,"bold"),fg="#FFD700",bg="#111111")
phone_entry.place(relx=0.6,rely=0.55,height=30,width=350)
date_entry = Entry(f2,font=("Verdana",12 ,"bold"),fg="#FFD700",bg="#111111")##########################
date_entry.place(relx=0.6,rely=0.65,height=30,width=270)#################################
btn_select_date = Button(f2, text="Select Date", command=open_calendar)########################
btn_select_date.place(relx= 0.88, rely=0.65 , height=30, width=70)#######################
btn_select_date.configure(fg="gold",bg="#111111")###################################
btn_done = Button(cal_frame, text="Done", command=get_selected_date)##########################
btn_done.pack()###########################
upload_button2 = Button(f2, text="UPLOAD", command=upload_profile_picture)
upload_button2.place(relx=0.115,rely=0.61)
upload_button2.configure(fg="gold",bg="#111111")

#updating records
def update_records():
    pass

#button to entry these records
Submit = Button(f2,text="SUBMIT", command = update_records,font=("Verdana",12 ,"bold"))
Submit.configure(activebackground="gold")
Submit.configure(cursor="hand2")
Submit.place(relx=0.85,rely=0.75,relheight=0.1,relwidth=0.1)
Submit.configure(fg="gold",bg="#111111")




# Close the cursor and connection
cursor.close()
connection.close()


root.mainloop()



# command la enna function kuduthurka 
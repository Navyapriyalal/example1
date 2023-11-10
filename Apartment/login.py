from essential import *
from tkinter import *
from PIL import Image, ImageTk
from next_login import Next_login


class Login:
    def __init__(self,root):
        self.root = root

        self.next_login = Next_login()

        self.f1 = Frame(root, bg="#666666")

        self.f2 = Frame(self.f1,bg = "black", height = 300 , width = 440)
        self.f2.place(relx=0.35, rely=0.35)

        self.heading= Label(self.f1, text="Log In", font=("Roboto", 32, "bold"),fg="#FFD700",bg="#666666")
        self.heading.place(relx=0.45,rely=0.20)

        self.user = Label(self.f2, text="Username", font=("Verdana",16 ,"bold"),fg="#FFD700",bg="black")    #user label
        self.password = Label(self.f2, text="Password", font=("Verdana",16 ,"bold"),fg="#FFD700",bg="black")    #password label
        self.user.place(relx=0.05,rely=0.05,width=140,height=30)     #relative positioning of label wrt self.f2
        self.password.place(relx=0.05,rely=0.35,width=140,height=30)

        self.username_val=StringVar()    #variable assigning for storing entries
        self.password_val=StringVar()

        self.userentry = Entry(self.f2, textvariable = self.username_val, borderwidth=2, relief="sunken", bg="grey", fg="#FFD700")     #entry box
        self.userentry.configure(font="-family Verdana -size 16")
        self.passentry = Entry(self.f2, textvariable = self.password_val, borderwidth=2, relief="sunken", bg="grey", fg="#FFD700")     #grid pack place are geometry manager must use only one   
        self.userentry.configure(font="-family Verdana -size 16")
        self.userentry.place(relx=0.05,rely=0.2,width=400,height=40)     #relative positioning of label wrt self.f2
        self.passentry.place(relx=0.05,rely=0.5,width=400,height=40)     #relative positioning of label wrt self.f2


        submit=Button(self.f2)      #submit-button 
        submit.configure(relief="flat")
        submit.configure(overrelief="raised")
        submit.configure(activebackground="grey")
        submit.configure(cursor="hand2")
        submit.configure(foreground="#FFD700")
        submit.configure(background="black")
        submit.configure(font="-family Verdana -size 16")
        submit.configure(borderwidth="0")
        submit.configure(text="SUBMIT")
        submit.configure(command=self.command_for_submit)
        submit.place(relx=0.05,rely=0.8,width=90,height=40)


    def command_for_submit(self):
        self.f1.pack_forget()
        print("start")
        self.next_login.f1.pack(side=TOP, expand = True, fill="both")
        print("closed")



        

        
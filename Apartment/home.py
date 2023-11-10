from essential import *
from tkinter import *
from PIL import Image, ImageTk




class Home():
    def __init__(self,root):
        self.root = root
        self.f1 = Frame(self.root, bg='#666666')
        self.f1.pack(side=TOP, expand = True, fill="both")

        self.heading = Label(self.f1, text="ABC\nApartments", font=("Roboto", 45, "bold"),fg="#FFD700",bg="#666666")
        self.heading.place(relx=0.39,rely=0.37)
        # self.background_img("images/home_bg.png")
        #self.f1.place(relx = 0, rely = 0,height=900,width=900)
    
    



        

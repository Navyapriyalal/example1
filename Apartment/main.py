from essential import *
from tkinter import *
from PIL import Image, ImageTk
from home import *
from login import Login


root = Tk()


 
def hide_all():
    home_page.f1.pack_forget()
    login_page.f1.pack_forget()
    # for widget in home_page.f1.winfo_children():
    #         widget.destroy()
    # for widget in login_page.Frame.winfo_children():
    #         widget.destroy()

def switch_home():
    hide_all()
    home_page.f1.pack(side=TOP, expand = True, fill="both")

def switch_login():
    hide_all()
    login_page.f1.pack(side=TOP, expand = True, fill="both")


def switch_community():
    hide_all()
    home_page.f1.pack(side=TOP, expand = True, fill="both")


root.geometry("1466x768")
root.maxsize(1466,768)
root.minsize(1466,768)
title_bar(root,"ABC BUILDERS")
menu(root,["HOME","COMMUNITY","LOGIN"],[LEFT,LEFT,RIGHT],[switch_home,community,switch_login])
home_page = Home(root)
login_page = Login(root)
community_page = Community(root)



root.mainloop()
#page to be shown after pressing announcement to community in user page
#page name - make_announcement

from essential import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tmsg
import mysql.connector
import io


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

#image carousel frame
f2 = Frame(f1)
f2.configure(bg="#333333")
f2.place(relx=0.62,rely=0.4,relheight=0.35,relwidth=0.35)

#content under due payment frame
maintenance = Label(f1)
maintenance.configure(text="YOUR ANNOUNCEMENT", font=("Roboto", 24, "bold"),fg="#FFD700",bg="#222222")
maintenance.place(relx=0.40, rely=0.25)

content = Text(f1)
content.place(relx=0.1,rely=0.4, relheight=0.4, relwidth=0.5)

list_path = []


def Pass():
    text_content = content.get("1.0", "end")  # Get text from line 1, character 0 to end
    print(text_content)

def Pics():
    i= len(list_path)
    if (i < 3) :
        file_path = filedialog.askopenfilename(filetypes=[('Image files', '*.png')])
        #opening the image in LBOB
        with open(file_path,'rb') as file:
            image_data = file.read()
        #appending the LBOB in a list
        list_path.append(image_data)

        #opening the image in the carousel
        image_obj = Image.open(file_path)
        resize_image = image_obj.resize((250,250))
        img= ImageTk.PhotoImage(resize_image)

        #creating label to show the pic
        gallery = Label(f2)
        gallery.image = img
        gallery['image'] = img
        gallery.place(relx=0.1,rely=0.0, relheight=1, relwidth=0.8)
    else:
        tmsg.showinfo("Alert","You can't upload more than 3 images!")
    return list_path

#carousel picture changing variable
i=0

def Right_carousel():
    global i
    i+=1
    index= i%len(list_path)
    image_obj = Image.open(io.BytesIO(list_path[index]))
    resize_image = image_obj.resize((250,250))
    img= ImageTk.PhotoImage(resize_image)

    #creating a label to display the profile picture.
    gallery = Label(f2)
    gallery.image = img
    gallery['image']=img
    gallery.place(relx=0.1,rely=0.0, relheight=1, relwidth=0.8)

def Left_carousel():
    global i
    i-=1
    index= i%len(list_path)
    image_obj = Image.open(io.BytesIO(list_path[index]))
    resize_image = image_obj.resize((250,250))
    img= ImageTk.PhotoImage(resize_image)

    #creating a label to display the profile picture.
    gallery = Label(f2)
    gallery.image = img
    gallery['image']=img
    gallery.place(relx=0.1,rely=0.0, relheight=1, relwidth=0.8)

#to move the carousel towards right
Right = Button(f2)
Right.place(relx= 0.96 , rely= 0.4)
Right.configure(text=">",height=3,width=1,bg="#111111")
Right.configure(command=Right_carousel)
Right.configure(activebackground="#555555")
Right.configure(cursor="hand2")

#to move the carousel towards left
Left = Button(f2)
Left.place(relx= 0.0 , rely= 0.4)
Left.configure(text="<",height=3,width=1,bg="#111111")
Left.configure(command=Left_carousel)
Left.configure(activebackground="#555555")
Left.configure(cursor="hand2")

#submit button
Submit = Button(f1)
Submit.pack()
Submit.place(relx= 0.60, rely=0.85)
Submit.configure(text="Submit",height=3, width=10, bg="gold", fg="black")
Submit.configure(command=Pass)
Submit.configure(activebackground="#333333")
Submit.configure(cursor="hand2")

Upload = Button(f1)
Upload.pack()
Upload.place(relx=0.75, rely=0.76)
Upload.configure(text="Upload pictures",height=2, width=12, bg="#111111", fg="black")
Upload.configure(command=Pics)
Upload.configure(activebackground="#333333")
Upload.configure(cursor="hand2")




cursor.close()
connection.close()


root.mainloop()




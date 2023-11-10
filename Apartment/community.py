from essential import *
from tkinter import *
from PIL import Image, ImageTk




class Community():
    def __init__(self,root):
        self.root = root
        self.f1 = Frame(self.root, bg='#666666')
        self.f1.pack(side=TOP, expand = True, fill="both")
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"Images\developer.jpg")
        img_top=img_top.resize((1530,720),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        # Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=700)

        img_top1=Image.open(r"Images\SUCHIR OK.jpg")
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=150)

        img_top2=Image.open(r"Images\DEEPAK KMR.jpg")
        img_top2=img_top2.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)
        f_lbl=Label(main_frame,image=self.photoimg_top2)
        f_lbl.place(x=300,y=150,width=200,height=170)

        img_top3=Image.open(r"Images\YASH TDN.jpg")
        img_top3=img_top3.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top3=ImageTk.PhotoImage(img_top3)
        f_lbl=Label(main_frame,image=self.photoimg_top3)
        f_lbl.place(x=300,y=320,width=200,height=200)

        img_top4=Image.open(r"Images\RICHA RAI.jpg")
        img_top4=img_top4.resize((200,200),Image.ANTIALIAS)
        self.photoimg_top4=ImageTk.PhotoImage(img_top4)
        f_lbl=Label(main_frame,image=self.photoimg_top4)
        f_lbl.place(x=300,y=510,width=200,height=190)

        # Developer info
        dev_label=Label(main_frame,text="Developers of this project are:",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=5,y=5)
        dev_label=Label(main_frame,text="Suchir Okram",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=50,y=70)
        dev_label=Label(main_frame,text="Deepak Kumar",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=45,y=200)
        dev_label=Label(main_frame,text="Yash Tandan",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=55,y=370)
        dev_label=Label(main_frame,text="Richa Rai",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=60,y=560)

        #img2=Image.open(r"C:\Users\Suchir Okram\Desktop\face_recognition_system\Images\developer2.jpg")
        #img2=img2.resize((500,390),Image.ANTIALIAS)
        #self.photoimg2=ImageTk.PhotoImage(img2)

        #f_lbl=Label(main_frame,image=self.photoimg2)
        #f_lbl.place(x=0,y=210,width=500,height=390)



if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
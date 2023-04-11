from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
#import random
#import time
#import datetime
import mysql.connector
import cv2
from main import Face_Recognition_System

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Suchir Okram\Desktop\face_recognition_system\Images\login1.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"Images\login-2.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(self.root,image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=120,height=100)

        title=Label(self.root,text="FACIAL RECOGNITION ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title.place(x=0,y=100,width=1550,height=45)

        # ============Project button(description)=====================
        downtitle=Label(self.root,text="Note: Enter valid username and valid password",font=("times new roman",25,"bold"),bg="white",fg="red")
        downtitle.place(x=0,y=740,width=1600,height=35)

        #img10=Image.open(r"Images\face-recognization-1.png")
        #img10=img10.resize((500,120),Image.ANTIALIAS)
        #self.photoimg10=ImageTk.PhotoImage(img10)
        #bg_lbl1=Label(bg_lbl,image=self.photoimg10)
        #bg_lbl1.place(x=0,y=0,width=500,height=120)

        #img11=Image.open(r"Images\face-recognization-1.png")
        #img11=img11.resize((500,120),Image.ANTIALIAS)
        #self.photoimg11=ImageTk.PhotoImage(img11)
        #bg_lbl2=Label(bg_lbl,image=self.photoimg11)
        #bg_lbl2.place(x=500,y=0,width=500,height=120)

        #img13=Image.open(r"Images\face-recognization-1.png")
        #img13=img13.resize((500,120),Image.ANTIALIAS)
        #self.photoimg13=ImageTk.PhotoImage(img13)
        #bg_lbl3=Label(bg_lbl,image=self.photoimg13)
        #bg_lbl3.place(x=1000,y=0,width=500,height=120)

        #frame=Frame(self.root,bg="black")
        #frame.place(x=610,y=200,width=340,height=430)

        #img1=Image.open(r"Images\face-recognization-1.png")
        #img1=img1.resize((500,120),Image.ANTIALIAS)
        #self.photoimage1=ImageTk.PhotoImage(img1)
        #bg_lbl2=Label(bg_lbl,image=self.photoimage1,bg="black",borderwidth=0)
        #bg_lbl2.place(x=730,y=200,width=90,height=90)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),bg="black",fg="white")
        get_str.place(x=95,y=100)

        # Label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),bg="black",fg="white")
        username.place(x=70,y=155)

        self.txtuser=StringVar()
        self.txtpass=StringVar()

        txtuser=ttk.Entry(frame,textvariable=self.txtuser,font=("times new roman",15,"bold"))
        txtuser.place(x=40,y=180,width=270)

        #txtuser=ttk.Entry(frame,textvariable=self.txtuser,font=("times new roman",15,"bold"))
        #txtuser.place(x=40,y=150,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="black",fg="white")
        password.place(x=70,y=225)

        txtpass=ttk.Entry(frame,textvariable=self.txtpass,font=("times new roman",15,"bold"),show="*")
        txtpass.place(x=40,y=250,width=270)

        # ================icon images===============
        img2=Image.open(r"Images\login-2.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"Images\lock.jpg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=395,width=25,height=25)

        # LoginButton
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RAISED,fg="white",bg="blue",activeforeground="white",activebackground="blue")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # RegisterButton
        registerbtn=Button(frame,text="New User Registration",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=26,y=350,width=160)

        # ForgotPasswButton
        forgotpassbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotpassbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields required!")
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome to VIT Bhopal")
        else:
            conn=mysql.connector.connect(host="127.0.0.1",username="root",password="saitama",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                                    ))
            row=my_cursor.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Authorized Person")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            self.clear()
            conn.close()
    
    def clear(self):
        self.txtuser.set("")
        self.txtpass.set("")
    #=============reset password======================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="127.0.0.1",username="root",password="saitama",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and SecurityQ=%s and SecurityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login new password",parent=self.root2)
                self.root2.destroy()

    #=================forgot password window=================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="127.0.0.1",username="root",password="saitama",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("My Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Pasword",font=("times new roman",20,"bold"),bg="white",fg="red")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Bestfriend name","Your pet name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ===============variables================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_SecurityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #=========bg image================
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Suchir Okram\Desktop\face_recognition_system\Images\register1.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #=========left image================
        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\Suchir Okram\Desktop\face_recognition_system\Images\register-1.jpeg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        # =============main frame===============
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        # ===============label and entry===============
        # ==========row1=====
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        # =========row2======
        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        # =========row3=======
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_SecurityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Bestfriend name","Your pet name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        # ===========row4===========
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #=========check button============
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree to the Terms and Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #========buttons=================
        img=Image.open(r"C:\Users\Suchir Okram\Desktop\face_recognition_system\Images\register-3.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
        b1.place(x=10,y=420,width=200)

        img1=Image.open(r"C:\Users\Suchir Okram\Desktop\face_recognition_system\Images\loginImg.png")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",12,"bold"))
        b1.place(x=330,y=420,width=200)

        # ================function declaration=============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_SecurityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="127.0.0.1",username="root",password="saitama",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists, please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_SecurityQ.get(),
                                                                                        self.var_SecurityA.get(),
                                                                                        self.var_pass.get(),
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")

    def return_login(self):
        self.root.destroy()


if __name__=="__main__":
    main()
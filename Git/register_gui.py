import time
from tkinter import messagebox

from customtkinter import *
from tkinter import *

from playsound import playsound

from main_gui import main_gui


def wait(delay):
    time.sleep(delay)


def register_gui():
    set_appearance_mode("light")
    set_default_color_theme("dark-blue")
    
    register_window = CTk()
    register_window.title("Register")
    register_window.geometry("1001x600+180+20")
    
    new_frame = CTkFrame(master=register_window)
    new_frame.configure(fg_color="white")
    new_frame.pack(padx=20, pady=20, fill="both", expand=True)
    
    register_frame = CTkFrame(master=new_frame)
    register_frame.configure(fg_color="#EDEDED")
    register_frame.place(x=500, y=30)

    # img_1 = PhotoImage(file="login.png")
    # login_image = Label(master=new_frame, image=img_1)
    # login_image.configure(background="white")
    # login_image.place(x=50, y=99)
    #
    # img2 = PhotoImage(file="user_image.png")
    # logo1 = Label(master=register_frame, image=img2)
    # logo1.configure(background="#EDEDED")
    
    register_label = CTkLabel(master=register_frame, text="Sign Up",
                              font=("Microsoft YaHei UI Light", 50, 'normal'),
                              text_color="#548BAF")
    register_label.pack(padx=140, pady=20)
    
    # logo1.pack(padx=10, pady=10)
    
    register_email_entry = CTkEntry(master=register_frame,
                                    placeholder_text="email or username:",
                                    height=40,
                                    width=230,
                                    border_width=0,
                                    font=("Microsoft YaHei UI Light", 24))
    register_email_entry.pack(padx=20, pady=20)
    
    register_password_entry = CTkEntry(master=register_frame,
                                       placeholder_text="password:",
                                       show='*',
                                       height=40,
                                       width=230,
                                       border_width=0,
                                       font=("Microsoft YaHei UI Light", 24))
    register_password_entry.pack(padx=20, pady=20)
    
    register_confirm_password_entry = CTkEntry(master=register_frame,
                                               placeholder_text="confirm password:",
                                               show='*',
                                               height=40,
                                               width=230,
                                               border_width=0,
                                               font=("Microsoft YaHei UI Light", 24))
    register_confirm_password_entry.pack(padx=20, pady=20)
    
    def optupdate(value):
        if value == "Light":
            set_appearance_mode("light")
            register_label.configure(text_color="#548BAF")
            # logo1.configure(background="#EDEDED")
            # login_image.configure(background="white")
            new_frame.configure(fg_color="white")
            register_frame.configure(fg_color="#EDEDED")
        
        elif value == "Dark":
            set_appearance_mode("dark")
            register_label.configure(text_color="lightblue")
 
            new_frame.configure(fg_color="#334742")
            register_frame.configure(fg_color="#192F32")
    
    optionmenu1 = CTkOptionMenu(master=new_frame, values=["Light", "Dark"], text_color="black",
                                font=("Microsoft YaHei UI Light", 13),
                                command=optupdate,
                                width=10, height=20)
    optionmenu1.place(x=5, y=520)
    
    def registration_complete():
        
        if len(register_email_entry.get()) > 0 and len(register_password_entry.get()) > 0:
            if register_confirm_password_entry.get() != register_password_entry.get():
                messagebox.showwarning("Password does not match!", "please check the password for confirming it.")
            
            else:
                register_email = register_email_entry.get()
                register_password_entry.get()
                confirm_password = register_confirm_password_entry.get()
                
                def signup():
                    file2 = open("registered_accounts.txt", 'w')
                    file2.write(f"' {register_email} : {confirm_password} : true '\n")
                    file2.close()
                
                wait(0)
                playsound("C:\\Users\\BITS\\Downloads\\interface-124464.mp3")
                signup()
                messagebox.showinfo("Registration Successful", "You're account is now registered!")
                register_window.destroy()
                wait(3)
                main_gui()
        
        else:
            messagebox.showwarning("Not filled entry", "please fill the entries!")
            register_window.mainloop()
    
    CTkButton(master=register_frame,
              height=40,
              width=250,
              text="Register",
              font=("Microsoft YaHei UI Light", 40),
              command=registration_complete) \
        .pack(padx=10, pady=25)
    
    register_window.mainloop()


register_gui()

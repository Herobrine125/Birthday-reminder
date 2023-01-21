from tkinter import PhotoImage, messagebox

from PIL import Image
from customtkinter import *


def main_gui():
    window = CTk(fg_color="#28314B")
    window.geometry("1200x650+80+20")
    window.title("Birthday reminder")
    icon_1 = PhotoImage(file="C:\\Users\\BITS\\Desktop\\Eashans projects\\Birthday reminder\\cake.png")
    window.iconphoto(False, icon_1)
    
    img_1 = CTkImage(Image.open("C:\\Users\\BITS\\Desktop\\Eashans projects\\Birthday reminder\\plus-icon.png")
                     .resize((20, 20)))
    img_2 = CTkImage(Image.open("C:\\Users\\BITS\\Desktop\\Eashans projects\\Birthday reminder\\home.png"),
                     size=(45, 45))
    img_3 = CTkImage(Image.open("C:\\Users\\BITS\\Desktop\\Eashans projects\\Birthday reminder\\cake.png"),
                     size=(50, 60))
    img_4 = CTkImage(Image.open("C:\\Users\\BITS\\Desktop\\Eashans projects\\Birthday reminder\\list.png"),
                     size=(45, 45))
    img_5 = CTkImage(Image.open("C:\\Users\\BITS\\Desktop\\Eashans projects\\Birthday reminder\\cake_2.png"),
                     size=(68, 50))
    img_6 = CTkImage(Image.open("C:\\Users\\BITS\\Desktop\\Eashans projects\\Birthday reminder\\settings.png"),
                     size=(45, 45))
    
    frame = CTkFrame(master=window, fg_color="#28314B")
    main_frame = CTkFrame(master=frame, height=630, width=880, fg_color="#D4D4D4")
    main_frame.place(x=300, y=0)
    tab_frame = CTkFrame(master=frame, height=630, width=290, fg_color="#D4D4D4")
    tab_frame.place(x=0, y=0)
    
    def home_page():
        home_frame = CTkFrame(master=main_frame, height=630, width=880, fg_color="#D4D4D4")
        home_frame.place(x=0, y=0)
        
        label_welcome = CTkLabel(master=home_frame, text="Welcome! ",
                                 font=("Microsoft YaHei", 50),
                                 text_color="black")
        label_welcome.place(x=250, y=30)
        
        CTkLabel(master=home_frame, text="Hello")
    
    def my_list_page():
        def add_remind():
            months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
                      "november", "december"]
            dialog_1 = CTkInputDialog(text="Name:", title="Create new remind")
            strout = dialog_1.get_input()
            dialog_1.destroy()
            dialog_2 = CTkInputDialog(text="Month:", title="Create new remind")
            strout_2 = dialog_2.get_input().lower()
            dialog_2.destroy()
            
            if strout_2 in months:
                print(strout, strout_2)
                CTkButton(master=my_list_frame, text=f"{strout}, {strout_2}").place(x=100, y=200)
            else:
                messagebox.showerror("Error", "Error! Could not get a matching input.")
        
        my_list_frame = CTkFrame(master=main_frame, height=630, width=880, fg_color="#D4D4D4")
        my_list_frame.place(x=0, y=0)
        
        add_button = CTkButton(master=my_list_frame, text="add new remind", image=img_1, compound=RIGHT,
                               command=add_remind)
        add_button.place(x=60, y=80)
    
    def settings_page():
        settings_frame = CTkFrame(master=main_frame, height=630, width=880, fg_color="#D4D4D4")
        settings_frame.place(x=0, y=0)
        
        label_1 = CTkLabel(master=settings_frame, text="Settings", font=("Microsoft YaHei UI Light", 60))
        label_1.place(x=300, y=10)
        
        label_2 = CTkLabel(master=settings_frame, text="Theme", font=("Microsoft YaHei", 26))
        label_2.place(x=40, y=160)
        
        def dark_mode():
            set_appearance_mode("dark")
            set_default_color_theme("lightgreen")
        
        CTkButton(master=settings_frame, text="Dark", font=("Microsoft YaHei", 20), text_color="black",
                  command=dark_mode).place(x=140, y=165)
    
    def delete_frames():
        for fr in main_frame.winfo_children():
            fr.destroy()
    
    def tabs(page):
        delete_frames()
        page()
    
    home_button = CTkButton(master=tab_frame, text=" Home  ", image=img_2, compound=LEFT,
                            font=("Microsoft YaHei UI Light", 40, "bold"),
                            height=80, width=302, fg_color="#D4D4D4", text_color="black",
                            hover_color="#BCBCBC",
                            command=lambda: tabs(home_page))
    home_button.place(x=-10, y=200)
    
    Logo = CTkLabel(master=tab_frame, image=img_3, text="The Birthday\nReminder!", compound=LEFT,
                    font=("Microsoft YaHei UI Light", 30, "bold"),
                    )
    Logo.place(x=20, y=20)
    
    Logo_2 = CTkButton(master=tab_frame, text="", image=img_5, compound=LEFT, fg_color="#D4D4D4", hover_color="#D4D4D4")
    Logo_2.place(x=75, y=130)
    
    my_list_button = CTkButton(master=tab_frame, text=" My lists", font=("Microsoft YaHei UI Light", 40, "bold"),
                               height=80, width=302, fg_color="#D4D4D4", text_color="black",
                               hover_color="#BCBCBC",
                               command=lambda: tabs(my_list_page),
                               image=img_4, compound=LEFT)
    my_list_button.place(x=-10, y=300)
    
    settings_button = CTkButton(master=tab_frame, text="Settings", font=("Microsoft YaHei UI Light", 40, "bold"),
                                height=60, width=302, fg_color="#D4D4D4", text_color="black",
                                hover_color="#BCBCBC",
                                command=lambda: tabs(settings_page),
                                image=img_6, compound=LEFT)
    settings_button.place(x=-10, y=570)
    
    frame.pack(padx=10, pady=10, fill="both", expand=True)
    
    window.mainloop()
    
    
main_gui()

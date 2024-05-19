import customtkinter as ctk
import socket
from Thingy import File_manager
from PIL import Image


def login_successful(user_level):
    root.destroy()
    File_manager(int(user_level))


def login_failed():
    popup = ctk.CTk()
    popup.geometry('200x100')
    label = ctk.CTkLabel(popup, text='Login failed, please try again.')
    label.pack(padx='10', pady='10')
    button = ctk.CTkButton(popup,text="OK",command=popup.destroy)
    button.pack()
    popup.mainloop()


def login_client(inputed_username, inputed_password):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 9999))

    message = client.recv(1024).decode()
    client.send(inputed_username.encode())
    message = client.recv(1024).decode()
    client.send(inputed_password.encode())

    user_level = client.recv(1024).decode()

    message = client.recv(1024).decode()
    
    if message == 'successful':
        login_successful(user_level)
    else:
        login_failed()


ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()
root.geometry('500x500')
root.title("ASU File Management")

frame = ctk.CTkFrame(root)
frame.pack(pady='30', padx='30',ipadx = 40,ipady=35)


path = "D:\\Coding\\Code\\Splash_scr_logo.png"


Logo = ctk.CTkImage(Image.open(path))
Logo._size = [150, 75]

label = ctk.CTkLabel(master=frame, image=Logo, text="")
label.pack(pady=12,ipadx = 20,ipady=20)

username_entery = ctk.CTkEntry(frame, placeholder_text='Username')
username_entery.pack(pady='10')

password_entery = ctk.CTkEntry(frame, placeholder_text='Password',show = "*")
password_entery.pack(pady='10', padx='30')


def login():
    inputed_username = username_entery.get()
    inputed_password = password_entery.get()

    if inputed_password != "" and inputed_username != "":
        login_client(inputed_username, inputed_password)
    
    else:
        toplevel21 = ctk.CTkToplevel()
        toplevel21.geometry('200x100')
        label21 = ctk.CTkLabel(toplevel21, text='Invalid Entry')
        label21.pack(padx='10', pady='10')
        button21 = ctk.CTkButton(toplevel21, text='Ok',command = toplevel21.destroy)
        button21.pack(padx='10', pady='10')
        toplevel21.mainloop()


login_button = ctk.CTkButton(frame, text='Login', command=login)
login_button.pack(pady='15')

quit = ctk.CTkButton(frame, text='Quit', command=root.destroy,fg_color="#817d80",hover_color="#3d3b3c")
quit.pack()

credit = ctk.CTkLabel(root,text="Made by Ammar & Saleh")
credit.pack(side = ctk.BOTTOM,pady = 2)

root.mainloop()

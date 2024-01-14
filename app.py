import customtkinter as ctk
import os
import configparser
import sys
from PIL import Image

#Fichier de configuration
config  = configparser.ConfigParser()
config.read('config.ini')

#Shortcuts
shortcut_a  = config['paths'].get('shortcut_a')
shortcut_b  = config['paths'].get('shortcut_b')
shortcut_c  = config['paths'].get('shortcut_c')
shortcut_d  = config['paths'].get('shortcut_d')

#Titles
title_a = config['titles'].get('title_a')
title_b = config['titles'].get('title_b')
title_c = config['titles'].get('title_c')
title_d = config['titles'].get('title_d')

#Icons
icon_a = config['icons'].get('icon_a')
icon_b = config['icons'].get('icon_b')
icon_c = config['icons'].get('icon_c')
icon_d = config['icons'].get('icon_d')
img1 = Image.open(icon_a)
img2 = Image.open(icon_b)
img3 = Image.open(icon_c)
img4 = Image.open(icon_d)

#Theme
theme = config['colors'].get("theme")

#Fonctions
def a():
    os.system(shortcut_a)
    sys.exit()

def b():
    os.system(shortcut_b)
    sys.exit()

def c():
    os.system(shortcut_c)   
    sys.exit()

def d():
    os.system(shortcut_d)
    sys.exit()

#GUI
ctk.set_appearance_mode(theme)
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title('Loupe')
app.geometry('350x500')
app.iconbitmap('assets/app/iconv2.ico')

logo = ctk.CTkImage(Image.open("assets/app/iconv2.png"), size=(130, 130))
logo = ctk.CTkLabel(app, image=logo, text=" ")
logo.place(x = 175, y = 80, anchor = "center")

button = ctk.CTkButton(app, command=a, image=ctk.CTkImage(img4, size=(28, 28)), width=200, height=50, corner_radius=80, text=title_a, font=("Helvetica", 20, "bold"), fg_color="#000493", hover_color="#00036d")
button.place(x= 175, y = 200, anchor=ctk.CENTER)
button = ctk.CTkButton(app, command=b, image=ctk.CTkImage(img4, size=(28, 28)), width=200, height=50, corner_radius=80, text=title_b, font=("Helvetica", 20, "bold"), fg_color="#000493", hover_color="#00036d")
button.place(x= 175, y = 280, anchor=ctk.CENTER)
button = ctk.CTkButton(app, command=c, image=ctk.CTkImage(img4, size=(28, 28)), width=200, height=50, corner_radius=80, text=title_c, font=("Helvetica", 20, "bold"), fg_color="#000493", hover_color="#00036d")
button.place(x= 175, y = 360, anchor=ctk.CENTER)
button = ctk.CTkButton(app, command=d, image=ctk.CTkImage(img4, size=(28, 28)), width=200, height=50, corner_radius=80, text=title_d, font=("Helvetica", 20, "bold"), fg_color="#000493", hover_color="#00036d")
button.place(x= 175, y = 440, anchor=ctk.CENTER)


#Démarrage du logiciel
app.resizable(False, False)
app.mainloop()
from tkinter import *
import customtkinter as ctk
import os
import configparser

#Fichier de configuration
config  = configparser.ConfigParser()
config.read('config.ini')

#Variables
shortcut_a  = config['paths'].get('shortcut_a')
shortcut_b  = config['paths'].get('shortcut_b')
shortcut_c  = config['paths'].get('shortcut_c')
shortcut_d  = config['paths'].get('shortcut_d')
title_a = config['gui'].get('title_a')
title_b = config['gui'].get('title_b')
title_c = config['gui'].get('title_c')
title_d = config['gui'].get('title_d')
theme = config['gui'].get("theme")

#Fonctions
def a():
    os.system(shortcut_a)
    app.quit()

def b():
    os.system(shortcut_b)
    app.quit()

def c():
    os.system(shortcut_c)   
    app.quit()

def d():
    os.system(shortcut_d)
    app.quit()

def quit():
    app.quit()

#UX
ctk.set_appearance_mode(theme)
ctk.set_default_color_theme("theme.json")
app = ctk.CTk()
app.title('Loupe')
app.geometry('350x500')

button = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text=title_a,
                                 command=a)
button.place(relx=0.5, rely=0.17, anchor=ctk.CENTER)

button = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text=title_b,
                                 command=b)
button.place(relx=0.5, rely=0.37, anchor=ctk.CENTER)

button = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text=title_c,
                                 command=c)
button.place(relx=0.5, rely=0.57, anchor=ctk.CENTER)

button = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text=title_d,
                                 command=d)
button.place(relx=0.5, rely=0.77, anchor=ctk.CENTER)

button = ctk.CTkButton(master=app,
                                fg_color='#A60325',
                                hover_color='#87031F',
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Quitter",
                                 command=quit)
button.place(relx=0.5, rely=0.95, anchor=ctk.CENTER)

#Démarrage du logiciel
app.mainloop()

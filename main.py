# main.py

# import lib
import tkinter as tk
import customtkinter as ctk
from lib.json import *
from lib.xml import *

ctk.set_appearance_mode("system")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

width, height = 1080, 720
app_geo = str(width) + "x" + str(height)

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry(app_geo)
app.title("Car Dictionary")
app.grid_rowconfigure(0, weight=1)
app.columnconfigure(2, weight=1)

title = ctk.CTkLabel(app, text="Car Dictionary")
title.pack()

side_view = ctk.CTkScrollableFrame(app, width=width/4, height=height)
side_view.pack(row = 0, column = 0)

app.mainloop()
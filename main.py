# main.py

# import lib
import tkinter as tk
import customtkinter as ctk
from lib.json import *
from lib.xml import *

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry("1080x720")

app.mainloop()
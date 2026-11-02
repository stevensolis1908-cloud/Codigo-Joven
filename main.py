import customtkinter as ctk
from importlib import import_module

vista_login = import_module("ventana").vista_login

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

ventana = ctk.CTk()
ventana.title("Código Joven - Iniciar sesión")
ventana.geometry("400x480")

vista_login(ventana)

ventana.mainloop()
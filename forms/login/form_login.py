import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.master.form_master import MasterPanel
from model.planilla_dao import *

class App:

    def verificar(self):
        usu = self.usuario.get()
        passw = self.password.get()
        if(usu == "pandora" and passw == "1234") :
            self.window.destroy()
            MasterPanel()
        elif(usu == "" and passw == ""):
            messagebox.showerror(message="Ingrese usuario y contraseña", title= "Error")
        elif(usu == ""):
            messagebox.showerror(message="Ingrese usuario", title= "Error")
        else:
            messagebox.showerror(message="La contraseña no es correcta", title= "Error")


    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Inicio de sesion")
        self.window.geometry('800x500')
        self.window.config(bg='#080808')
        self.window.resizable(width=0, height=0)
        utl.centrar_ventana(self.window, 800, 500)
        
        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))

        #panel logo
        frame_logo = tk.Frame(self.window, bd=0, relief=tk.SOLID, padx=10, pady=10, bg='#17202A')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#17202A')
        label.place(relwidth=1, relheight=1)
        #panel_form
        frame_form = tk.Frame(self.window, bd=0, relief=tk.SOLID, bg='#17202A')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
    
        #contenido form
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#17202A')
        frame_form_top.pack(fill=tk.X,pady=20)

        title = tk.Label(frame_form_top, text="Login", font=('Open Sans', 20, BOLD), fg="#fff", bg="#17202A", pady=50)
        title.pack(expand=tk.YES)
        #panel_login_llenar
        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#17202A')
        frame_form_fill.pack(pady=5,expand=tk.YES, fill=tk.BOTH)

        frame_form_usuario = tk.Frame(frame_form_fill,height=50,bd=0, relief=tk.SOLID, bg='#17202A')
        frame_form_usuario.pack(pady=5)

        etiqueta_usuario = tk.Label(frame_form_usuario, text="Usuario", font=("Open Sans", 10, BOLD), fg="#ffffff",bg="#17202A")
        etiqueta_usuario.pack(side="left")
        self.usuario = tk.Entry(frame_form_usuario, font=("Open Sans", 10))
        self.usuario.pack()

    
        frame_form_password = tk.Frame(frame_form_fill,height=50,bd=0, relief=tk.SOLID, bg='#17202A')
        frame_form_password.pack(padx=10,pady=5)

        etiqueta_password = tk.Label(frame_form_password, text="Contraseña", font=("Open Sans", 10, BOLD), fg="#ffffff",bg="#17202A")
        etiqueta_password.pack(side="left")
        self.password = tk.Entry(frame_form_password, font=("Open Sans", 10))
        self.password.pack()
        self.password.config(show="*")

        frame_form_boton = tk.Frame(frame_form_fill,height=50,bd=0, relief=tk.SOLID, bg='#17202A')
        frame_form_boton.pack()

        inicio = tk.Button(frame_form_boton,  text="Iniciar sesion", font=("Open Sans", 10, BOLD),bg="#C0392B", bd=0, fg="#fff", command=self.verificar)
        inicio.pack(side="left",padx=5,pady=10)
        salir = tk.Button(frame_form_boton, text="Salir", font=("Open Sans", 10, BOLD),bg="#C0392B", bd=0, fg="#fff", command=self.window.destroy)
        salir.pack(padx=5,pady=10)

        creardb = tk.Button(frame_form, text='Crear db', command=crear_tabla)
        creardb.pack()
        eliminardb = tk.Button(frame_form, text='Borrar db', command=borrar_tabla)
        eliminardb.pack()


        inicio.bind("<Return>", (lambda event: self.verificar()))


        self.window.mainloop()
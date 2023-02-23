import tkinter as tk
import ttkbootstrap as tb
import util.generic as utl


class MasterPanel:

    def __init__(self):

        def abrir_ventana():

            def limitar_caracteres(*args):
                if len(limitarcaracteres.get()) > 6:
                    limitarcaracteres.set(limitarcaracteres.get()[:6])

            limitarcaracteres = tb.StringVar()
            limitarcaracteres.trace("w", limitar_caracteres)      

            def convertir_mayusculas(*args):
                todomayuscula.set(todomayuscula.get().upper())
            
            todomayuscula = tb.StringVar()
            todomayuscula.trace("w", convertir_mayusculas)

            

            ventana = tb.Toplevel("Full CarWash - Generar Servicio", resizable=(False, False))
            ventana.iconbitmap('imagenes/logochiquito.ico')
            # Obtener el ancho y la altura de la pantalla del usuario
            ancho_pantalla = ventana.winfo_screenwidth()
            altura_pantalla = ventana.winfo_screenheight()

            # Obtener el ancho y la altura de la ventana
            ancho_ventana = ventana.winfo_width()
            altura_ventana = ventana.winfo_height()

            # Calcular la posición x e y para la ventana
            pos_x = int((ancho_pantalla - ancho_ventana) / 3)
            pos_y = int((altura_pantalla - altura_ventana) / 5)

            # Establecer la posición de la ventana
            ventana.geometry(f"+{pos_x}+{pos_y}")
            ventana.grab_set()
            #agregar metodo destroy() despues de insterar los datos, si no,la pantalla quedara bloqueada
            ##limitar caracteres para patente

            framecontenedor = tb.Frame(ventana)
            framecontenedor.pack(pady=20,padx=10)

            #frametitulo = tb.Frame(framecontenedor)
            #frametitulo.grid(column=0, row=0)
            
            #label1 = tb.Label(frametitulo, text='Generar Servicio', font=(20))
            #label1.pack(padx=50,pady=30)
            ##DATOS CLIENTE
            frameentry1 = tb.Frame(framecontenedor)
            frameentry1.grid(column=0, row=1, columnspan=2, sticky='nsew')

            lfcliente = tb.LabelFrame(frameentry1, text='Datos Cliente')
            lfcliente.pack(padx=10,pady=10, fill='both', expand=True)

            label2 = tb.Label(lfcliente, text='NOMBRE (APODO)')
            #label2.pack(padx=10,pady=10, side='left')
            label2.grid(padx=10,pady=10,row=0,column=0)

            entry1 = tb.Entry(lfcliente, width=50, textvariable=todomayuscula)
            #entry1.pack(padx=10,pady=10, side='right')
            entry1.grid(padx=10,pady=10, row=0,column=1, sticky='w')
            
            #frameentry2 = tb.Frame(framecontenedor)
            #frameentry2.grid(column=0, row=2)

            label3 = tb.Label(lfcliente, text='TELEFONO')
            #label3.pack(padx=10,pady=10, side='left')
            label3.grid(padx=10,pady=10, row=1,column=0)

            entry2 = tb.Entry(lfcliente, width=30)
            #entry2.pack(padx=10,pady=10, side='right')
            entry2.grid(padx=10,pady=10, row=1,column=1, sticky='w')

            ##INFORMACION DEL VEHICULO
            frameentry3 = tb.Frame(framecontenedor)
            frameentry3.grid(column=0, row=3, columnspan=2, sticky='nsew')

            lbvehiculo = tb.LabelFrame(frameentry3, text='Informacion del Vehiculo')
            lbvehiculo.pack(padx=10,pady=10, fill='both', expand='yes')

            label4 = tb.Label(lbvehiculo, text='TIPO DE VEHICULO')
            label4.grid(padx=10,pady=10, row=0,column=0, sticky='w')

            entry3 = tb.Combobox(lbvehiculo, width=20, justify='center', values=(
                '----autos', 'sedan corto', 'sedan', 'sedan largo', 
                '----suv', 'suv pequeña', 'suv 2 corridas', 'suv 2 corridas grande', 'suv 3 corridas',
                '----todoterreno', 'jeep pequeño'
                'camioneta 4x4'), state='readonly')
            entry3.grid(padx=10,pady=10, row=0,column=1, sticky='w')

            labelpatente = tb.Label(lbvehiculo, text='PATENTE')
            labelmodelo = tb.Label(lbvehiculo, text='MODELO')
            labelcolor = tb.Label(lbvehiculo, text='COLOR')
            entrypatente = tb.Entry(lbvehiculo, textvariable=limitarcaracteres)
            entrymodelo = tb.Entry(lbvehiculo)
            entrycolor = tb.Entry(lbvehiculo)
            labelpatente.grid(padx=10,pady=10, row=1,column=0, sticky='w')
            labelmodelo.grid(padx=10,pady=10, row=2,column=0, sticky='w')
            labelcolor.grid(padx=10,pady=10, row=2,column=2, sticky='w')
            entrypatente.grid(padx=10,pady=10, row=1,column=1, sticky='w')
            entrymodelo.grid(padx=10,pady=10, row=2,column=1, sticky='w')
            entrycolor.grid(padx=10,pady=10, row=2,column=3, sticky='w')

            ##INFORMACION DEL SERVICIO
            frameentry4 = tb.Frame(framecontenedor)
            lfinfos = tb.LabelFrame(frameentry4,text='Informacion del Servicio')
            label5 = tb.Label(lfinfos, text='SERVICIO')
            rb1 = tb.Radiobutton(lfinfos, text='FULL', variable=False, value=0)
            rb2 = tb.Radiobutton(lfinfos, text='Sólo por FUERA', variable=False, value=1)
            rb3 = tb.Radiobutton(lfinfos, text='Sólo por DENTRO', variable=False, value=2)
            lblnotas = tb.Label(lfinfos, text='NOTAS')
            entnotas = tb.Entry(lfinfos, width=67)

            frameentry4.grid(column=0, row=4, columnspan=2, sticky='nsew')
            lfinfos.pack(padx=10,pady=10, fill='both', expand='yes')
            label5.grid(padx=10,pady=10, row=0,column=0, sticky='w')
            rb1.grid(padx=10,pady=10, row=0,column=1)
            rb2.grid(padx=10,pady=10, row=0,column=2)
            rb3.grid(padx=10,pady=10, row=0,column=3)
            lblnotas.grid(padx=10,pady=10, row=1,column=0, sticky='w')
            entnotas.grid(padx=10, pady=10, row=1, column=1,columnspan=3)

            ##VALOR Y DESCUENTO
            framevalor = tb.Frame(framecontenedor)
            lfvalor = tb.LabelFrame(framevalor, text='Valor y descuento del servicio')
            lbldct = tb.Label(lfvalor, text='DESCUENTO')
            entdct = tb.Entry(lfvalor, state='false')
            framevalorf = tb.Frame(framecontenedor)
            lfvalorf = tb.LabelFrame(framevalorf, text='$$')
            lblvalorf = tb.Label(lfvalorf, text= 'Valor', font=('Comic Sans', 11))
            lblvalornum = tb.Label(lfvalorf, text='$10.000', font=('Comic Sans', 11))
            lblvalordcto = tb.Label(lfvalorf, text='Dcto', font=('Comic Sans', 11))
            lblvalordctonum = tb.Label(lfvalorf, text='$3.000', font=('Comic Sans', 11), style='danger')
            lblvalorfinal = tb.Label(lfvalorf, text='Total a pagar', font=('Comic Sans', 12, 'bold'))
            lblvalorfinalnum = tb.Label(lfvalorf, text='$7.000', font=('Comic Sans', 12, 'bold'))

            framevalor.grid(column=0, row=5, sticky='nsew')
            lfvalor.pack(padx=10,pady=10, side='left', fill='both')
            lbldct.grid(padx=10, pady=10, row=0, column=0)
            entdct.grid(padx=10, pady=10, row=0, column=1)
            framevalorf.grid(padx=10,pady=10, column=0, row=6, sticky='nsew')
            lfvalorf.pack(padx=10,pady=10, fill='both')
            lblvalorf.grid(padx=10, pady=1, row=0, column=0, sticky='e')
            lblvalornum.grid(padx=10, pady=1, row=0, column=1, sticky='w')
            lblvalordcto.grid(padx=10, pady=1, row=1, column=0, sticky='e')
            lblvalordctonum.grid(padx=10, pady=1, row=1, column=1, sticky='w')
            lblvalorfinal.grid(padx=10, pady=1, row=2, column=0, sticky='e')
            lblvalorfinalnum.grid(padx=10, pady=1, row=2, column=1, sticky='w')

            framevalorf.columnconfigure(0, weight=1)
            framevalorf.columnconfigure(1, weight=1)
            framevalorf.rowconfigure(0, weight=1)
            framevalorf.rowconfigure(1, weight=1)
            framevalorf.rowconfigure(2, weight=1)

            ##BOTONES ACEPTER Y CANCELAR

            fmbotones = tb.Frame(framecontenedor)
            btaceptar = tb.Button(fmbotones, style='success', text='Aceptar')
            btcancelar = tb.Button(fmbotones, style='danger',text='Cancelar')

            fmbotones.grid(row=6,column=1)
            btcancelar.pack(padx=10, pady=10, anchor='e' , side='right')
            btaceptar.pack(padx=10, pady=10, anchor='e' ,side='right')





        self.window = tb.Window(themename="darkly")
        self.window.iconbitmap('imagenes/logochiquito.ico')
        self.window.title("Full CarWash")
        self.window.minsize('1000','800')
        #w, h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()
        #self.window.geometry("%dx%d+0+0" % (w, h))
        #self.window.geometry('1600x900')
        #self.window.config(bg='#17202A')
        #self.window.resizable()

        framep = tb.Frame(self.window)
        framep.pack(fill="both", expand=True)

        frame2 = tb.Frame(framep, padding=20)
        frame2.grid(column=0, row=0)

        frame1 = tb.Frame(framep, padding=20)
        frame1.grid(column=1, row=0, sticky='e')

        #cosas frame1
        tabla = tb.Treeview(frame1,columns=('vehiculo', 'patente', 'hora ingreso', 'cliente', 'telefono'), height=45)
        tabla.pack(padx=5, pady=5, ipady=5, expand=True, fill="both")
        tabla.heading('#0', text='ID')
        tabla.heading('#1', text='VEHICULO')
        tabla.heading('#2', text='Patente')
        tabla.heading('#3', text='HORA INGRESO')
        tabla.heading('#4', text='Cliente')
        tabla.heading('#5', text='Telefono')
        tabla.insert('' , 0, text='01', values=('audi TT', 'HHGG99', '12:40', 'Marcos', '998886665'))
        tabla.column('#0', width=50,minwidth=50)
        tabla.column('#1', width=100,minwidth=100)
        tabla.column('#2', width=100,minwidth=100)
        tabla.column('#3', width=100,minwidth=100)
        tabla.column('#4', width=100,minwidth=100)
        tabla.column('#5', width=100,minwidth=100)

        tabla.tag_configure('01', foreground='red')


        


        madeby = tb.Label(text='Version Alpha 1.0.0     -     Made by Pandorita ❤️', font=('Open Sans', 10,'italic' ))
        madeby.pack()
        #cosas frame2
        framecalendario= tb.Frame(frame2)
        framecalendario.pack(side='top', pady=20)
        labelx = tb.Label(framecalendario, text='FECHA')
        calendario = tb.DateEntry(framecalendario, bootstyle='danger')
        labelx.grid(row=0,column=0, sticky='w',padx=10)
        calendario.grid(row=0,column=1, sticky='w',padx=10)

        bt_nuevoservicio = tb.Button(frame2, text='NUEVO SERVICIO', bootstyle="sucess", width=50, command=abrir_ventana)
        bt_nuevoservicio.pack(padx=5, pady=5, ipady=5, expand=True, fill="both")
        bt_cancelarservicio = tb.Button(frame2, text='CANCELAR SERVICIO', bootstyle="sucess", width=20)
        bt_cancelarservicio.pack(pady=5, padx=5, ipady=5, expand=True, fill="both")
        bt_entregar = tb.Button(frame2, text='ENTREGAR SERVICIO', bootstyle="warning", width=20)
        bt_entregar.pack(pady=5, padx=5, ipady=5, expand=True, fill="both")
        bt_designar = tb.Button(frame2, text='DESIGNAR LAVADOR', bootstyle="light", width=20)
        bt_designar.pack(pady=5, padx=5, ipady=5, expand=True, fill="both")
        bt_eliminarservicio = tb.Button(frame2, text='ELIMINAR SERVICIO', bootstyle="danger", width=20)
        bt_eliminarservicio.pack(pady=5, padx=5, ipady=5, expand=True, fill="both")
        bt_editarservicio = tb.Button(frame2, text='EDITAR SERVICIO', bootstyle="light", width=20)
        bt_editarservicio.pack(pady=5, padx=5, ipady=5, expand=True, fill="both")
        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        label = tb.Label(frame2, image=logo)
        label.pack()

        

        self.window.mainloop()
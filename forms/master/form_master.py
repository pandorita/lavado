import tkinter as tk
import ttkbootstrap as tb
import util.generic as utl


class MasterPanel:

    def __init__(self):

        def abrir_ventana():
            ventana = tb.Toplevel("Generar Servicio", resizable=(False, False))
            ventana.iconbitmap('imagenes/logochiquito.ico')
            ventana.grab_set()
            #agregar metodo destroy() despues de insterar los datos, si no,la pantalla quedara bloqueada

            framecontenedor = tb.Frame(ventana)
            framecontenedor.pack()

            #frametitulo = tb.Frame(framecontenedor)
            #frametitulo.grid(column=0, row=0)
            
            #label1 = tb.Label(frametitulo, text='Generar Servicio', font=(20))
            #label1.pack(padx=50,pady=30)

            frameentry1 = tb.Frame(framecontenedor)
            frameentry1.grid(column=0, row=1)

            lfcliente = tb.LabelFrame(frameentry1, text='Datos Cliente')
            lfcliente.pack(padx=10,pady=10, fill='both', expand='yes')

            label2 = tb.Label(lfcliente, text='NOMBRE O APODO CLIENTE')
            #label2.pack(padx=10,pady=10, side='left')
            label2.grid(padx=10,pady=10,row=0,column=0)

            entry1 = tb.Entry(lfcliente, width=50)
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

            frameentry3 = tb.Frame(framecontenedor)
            frameentry3.grid(column=0, row=3)

            label4 = tb.Label(frameentry3, text='TIPO DE VEHICULO')
            label4.pack(padx=10,pady=10, side= 'left')

            entry3 = tb.Combobox(frameentry3, width=30, justify='center', values=(
                '----autos', 'sedan corto', 'sedan', 'sedan largo', 
                '----suv', 'suv pequeña', 'suv 2 corridas', 'suv 2 corridas grande', 'suv 3 corridas',
                '----todoterreno', 'jeep pequeño'
                'camioneta 4x4'), state='readonly')
            entry3.pack(padx=10,pady=10, side= 'left')

            frameentry4 = tb.Frame(framecontenedor)
            frameentry4.grid(column=0, row=4)

            label5 = tb.Label(frameentry4, text='SERVICIO')
            label5.pack(padx=10,pady=10, side= 'left')

            rb1 = tb.Radiobutton(frameentry4, text='FULL', variable=False, value=0)
            rb1.pack(padx=10,pady=10, side= 'left')
            rb2 = tb.Radiobutton(frameentry4, text='Sólo por FUERA', variable=False, value=1)
            rb2.pack(padx=10,pady=10, side= 'left')
            rb3 = tb.Radiobutton(frameentry4, text='Sólo por DENTRO', variable=False, value=2)
            rb3.pack(padx=10,pady=10, side= 'left')






        self.window = tb.Window(themename="darkly")
        self.window.iconbitmap('imagenes/logochiquito.ico')
        self.window.title("FULL CAR WASH")
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
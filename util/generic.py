from PIL import ImageTk, Image

def leer_imagen(path, size):
        return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ANTIALIAS))


def centrar_ventana(ventana, aplicacion_ancho , aplicacion_largo):
    window_ancho = ventana.winfo_screenwidth()
    window_largo = ventana.winfo_screenheight()
    x = int((window_ancho/2) - (aplicacion_ancho/2))
    y = int((window_largo/2) - (aplicacion_largo/2))
    return ventana.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")
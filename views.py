from tkinter import Tk, Frame, Label, Button
from tkinter.font import Font
from PIL import Image, ImageTk
from models import Evento, Ruta_visita, Ubicacion, Usuario, Review

def resize_image(event):
    global background_photo

    # Redimensionar imagen según el tamaño de la ventana
    ancho = event.width
    alto = event.height
    background_image_resized = background_image.resize((ancho, alto), Image.ANTIALIAS)
    background_photo = ImageTk.PhotoImage(background_image_resized)
    background_label.config(image=background_photo)

def mostrar_indice_eventos():
    # Lógica para mostrar el índice de eventos
    # Actualiza los componentes de la interfaz gráfica con la información de los eventos
    for evento in eventos:
        evento_label = Label(content_frame, text=f"Nombre: {evento.nombre}, Artista: {evento.artista}")
        evento_label.pack()

def mostrar_busqueda_eventos():
    # Lógica para mostrar la búsqueda y filtrado de eventos
    # Implementa la lógica de búsqueda y filtrado según tus necesidades
    pass

def mostrar_historial_eventos():
    # Lógica para mostrar el historial de eventos
    # Actualiza los componentes de la interfaz gráfica con la información del historial de eventos del usuario
    for evento in usuario1.historial_eventos:
        evento_label = Label(content_frame, text=f"Nombre: {evento.nombre}, Artista: {evento.artista}")
        evento_label.pack()

root = Tk()
root.geometry("800x600")

background_image = Image.open("/home/pablo/Documentos/Programación/1000 programadores salteños/Tour musical/assets/images/Salta_1.jpeg")
background_photo = ImageTk.PhotoImage(background_image)

titulo_font = Font(family='Roboto', size=16, weight='bold')
texto_font = Font(family='Open Sans', size=12)

content_frame = Frame(root)
content_frame.place(x=0, y=0, relwidth=1, relheight=1)

background_frame = Frame(content_frame)
background_frame.place(x=0, y=0, relwidth=1, relheight=1)

titulo_label = Label(content_frame, text='Tour Musical', font=titulo_font)
titulo_label.pack(pady=20)

indice_eventos_button = Button(content_frame, text='Índice de Eventos', font=texto_font, command=mostrar_indice_eventos)
indice_eventos_button.pack(pady=10)

busqueda_button = Button(content_frame, text='Búsqueda y Filtrado de Eventos', font=texto_font, command=mostrar_busqueda_eventos)
busqueda_button.pack(pady=10)

historial_button = Button(content_frame, text='Historial de Eventos', font=texto_font, command=mostrar_historial_eventos)
historial_button.pack(pady=10)

background_label = Label(background_frame, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

root.bind("<Configure>", resize_image)
root.mainloop()

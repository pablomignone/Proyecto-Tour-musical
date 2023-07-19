class Evento:
    def __init__(self, id, nombre, artista, genero, id_ubicacion, hora_inicio, hora_fin, descripcion, imagen):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen

class Ruta_visita:
    def __init__(self, id, nombre, destinos):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

class Ubicacion:
    def __init__(self, id, nombre, direccion, coordenadas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.coordenadas = coordenadas

class Usuario:
    def __init__(self, id, nombre, apellido, historial_eventos):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_eventos = historial_eventos

class Review:
    def __init__(self, id, id_evento, id_usuario, calificacion, comentario, animo):
        self.id = id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

#Crear Eventos
# Crear un evento para Alan Sutton y las criaturitas de la ansiedad
evento1 = Evento(
    id = 1,
    nombre = "Alan Sutton y las criaturitas de la ansiedad",
    artista = "Alan Sutton y las criaturitas de la ansiedad",
    genero = "Rock alternativo",
    id_ubicacion = 1,
    hora_inicio = "21:00",
    hora_fin = "23:00",
    descripcion = "Una noche de rock alternativo con la banda liderada por Alan Sutton, que presenta su nuevo disco 'La vida es un sueño'.",
    imagen = "alan_sutton.jpg"
)

# Crear un evento para El Cuarteto de Nos
evento2 = Evento(
    id = 2,
    nombre = "El Cuarteto de Nos",
    artista = "El Cuarteto de Nos",
    genero = "Rock",
    id_ubicacion = 2,
    hora_inicio = "20:00",
    hora_fin = "22:00",
    descripcion = "Disfruta del humor y la música de la banda uruguaya El Cuarteto de Nos, que llega a Salta con su gira 'Jueves'.",
    imagen = "el_cuarteto_de_nos.jpg"
)

# Crear un evento para Homer El Mero Mero
evento3 = Evento(
    id = 3,
    nombre = "Homer El Mero Mero",
    artista = "Homer El Mero Mero",
    genero = "Hip hop",
    id_ubicacion = 2,
    hora_inicio = "19:00",
    hora_fin = "21:00",
    descripcion = "No te pierdas el show de Homer El Mero Mero, el rapero argentino que está revolucionando la escena del hip hop con su flow y sus letras.",
    imagen = "homer_el_mero_mero.jpg"
)
evento4 = Evento(
    id = 4,
    nombre = "14º Festival La Troja Canta",
    artista = "Varios",
    genero = "Folclore",
    id_ubicacion = 3,
    hora_inicio = "18:00",
    hora_fin = "02:00",
    descripcion = "Un festival para celebrar la música y la cultura folclórica de Salta, con la participación de artistas locales e invitados especiales.",
    imagen = "la_troja_canta.jpg"
)

# Crear una ubicación para El teatrino
ubicacion1 = Ubicacion(
    id = 1,
    nombre = "El Teatrino",
    direccion = "Aniceto Latorre y Alvear",
    coordenadas = (-24.7909, -65.4117)
)

# Crear una ubicación para el Teatro Provincial de Salta
ubicacion2 = Ubicacion(
    id = 2,
    nombre = "Teatro Provincial de Salta",
    direccion = "Zuviría 70",
    coordenadas = (-24.7888, -65.4105)
)

ubicacion3 = Ubicacion(
    id = 3,
    nombre = "La Troja",
    direccion = "Paraje La Troja, Salta",
    coordenadas = ( -24.7859, -65.41166)
)

# Crear una ruta de visita con los tres conciertos
ruta1 = Ruta_visita(
    id = 1,
    nombre = "Ruta rockera",
    destinos = [evento2, evento3, evento4]
)

# Crear una ruta de visita con los eventos folclóricos
ruta2 = Ruta_visita(
    id = 2,
    nombre = "Ruta folklórica",
    destinos = [evento4]
)

# Crear un usuario con los datos de ejemplo
usuario1 = Usuario(
    id = 1,
    nombre = "Juan",
    apellido = "Pérez",
    historial_eventos = [evento2, evento4]
)

# Crear una review con los datos de ejemplo
review1 = Review(
    id = 1,
    id_evento = 1,
    id_usuario = 1,
    calificacion = 5,
    comentario = "Me encantó el concierto de Alan Sutton y las criaturitas de la ansiedad. Fue una noche increíble, con buena música y buen ambiente. La banda sonó genial y el público se prendió con cada tema. Recomiendo este evento a todos los que les gusta el rock alternativo.",
    animo = "Feliz"
)

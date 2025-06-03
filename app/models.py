from pydantic import BaseModel

class Libro:

    #Clase que representa un libro en el sistema.

    def __init__(self, id: int, titulo: str, autor: str, anio: int, descripcion: str = None):
        self._id = id
        self._titulo = titulo
        self._autor = autor
        self._anio = anio
        self._descripcion = descripcion

    @property
    def id(self) -> int:
        return self._id

    @property
    def titulo(self) -> str:
        return self._titulo

    @titulo.setter
    def titulo(self, nuevo_titulo: str):
        if not nuevo_titulo:
            raise ValueError("El título no puede estar vacío")
        self._titulo = nuevo_titulo

    @property
    def autor(self) -> str:
        return self._autor

    @autor.setter
    def autor(self, nuevo_autor: str):
        if not nuevo_autor:
            raise ValueError("El autor no puede estar vacío")
        self._autor = nuevo_autor

    @property
    def anio(self) -> int:
        return self._anio

    @anio.setter
    def anio(self, nuevo_anio: int):
        if nuevo_anio < 0:
            raise ValueError("El año no puede ser negativo")
        self._anio = nuevo_anio

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, nueva_desc: str):
        if not nueva_desc:
            raise ValueError("La descripcion no puede estar vacío")
        self._autor = nueva_desc


    def to_dict(self) -> dict:

        #Convierte la instancia a diccionario.

        return {
            "id": self._id,
            "titulo": self._titulo,
            "autor": self._autor,
            "anio": self._anio,
            "descripcion": self._descripcion
        }
    
#Esquema para creación de libro
class LibroCreate(BaseModel):
    titulo: str
    autor: str
    anio: int
    descripcion: str = None

#Esquema para actualización de libro
class LibroUpdate(BaseModel):
    titulo: str = None
    autor: str = None
    anio: int = None
    descripcion: str = None

# Esquema para respuesta
class LibroRead(BaseModel):
    id: int
    titulo: str
    autor: str
    anio: int
    descripcion: str = None

    class Config:
        orm_mode = True
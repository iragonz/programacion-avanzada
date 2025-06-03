from app.models import Libro
from typing import List

class GestorLibros:

    #Clase que encapsula la lógica de almacenamiento de libros en memoria.

    def __init__(self):
        self._libros: List[Libro] = []  # lista interna de objetos Libro
        self._contador_id: int = 1      # contador interno para asignar IDs únicos

    def listar_libros(self) -> List[dict]:
        """
        Devuelve la lista de libros en forma de lista de diccionarios.
        """
        return [libro.to_dict() for libro in self._libros]

    def obtener_libro(self, id_libro: int) -> dict:

        #Busca un libro por su ID.

        for libro in self._libros:
            if libro.id == id_libro:
                return libro.to_dict()
        return None

    def crear_libro(self, titulo: str, autor: str, anio: int, descripcion: str = None) -> dict:

        # Crea un libro nuevo, lo agrega a la lista interna y retorna su representación.

        nuevo = Libro(
            id=self._contador_id,
            titulo=titulo,
            autor=autor,
            anio=anio,
            descripcion=descripcion
        )
        self._libros.append(nuevo)
        self._contador_id += 1
        return nuevo.to_dict()

    def actualizar_libro(self, id_libro: int, titulo: str = None,
                         autor: str = None,
                         anio: int = None,
                         descripcion: str = None) -> dict:

        #Actualiza los campos de un libro existente. Retorna el libro modificado o None si no se encontró.

        for libro in self._libros:
            if libro.id == id_libro:
                # Solo actualizamos si el campo no es None
                if titulo is not None:
                    libro.titulo = titulo
                if autor is not None:
                    libro.autor = autor
                if anio is not None:
                    libro.anio = anio
                if descripcion is not None:
                    libro.descripcion = descripcion
                return libro.to_dict()
        return None

    def eliminar_libro(self, id_libro: int) -> bool:

        #Elimina un libro por su ID. Retorna True si fue eliminado, o False si no existía.

        for idx, libro in enumerate(self._libros):
            if libro.id == id_libro:
                del self._libros[idx]
                return True
        return False

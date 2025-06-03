
from fastapi import FastAPI, HTTPException
from typing import List
from app.manager import GestorLibros
from app.models import LibroCreate, LibroUpdate, LibroRead

app = FastAPI(
    title="API de Gestión de Libros",
    description="Creación, lectura, actualización y eliminación de libros.",
    version="1.0.0"
)

# Instancia única de gestor
gestor = GestorLibros()

# Listar todos los libros (GET)
@app.get("/libros", response_model=List[LibroRead])
def listar_todos():

    return gestor.listar_libros()


# Listar un libro por ID (GET)
@app.get("/libros/{id_libro}", response_model=LibroRead)
def obtener_por_id(id_libro: int):

    libro = gestor.obtener_libro(id_libro)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro


# Crear un libro (POST)
@app.post("/libros", response_model=LibroRead, status_code=201)
def crear_libro(libro_in: LibroCreate):

    creado = gestor.crear_libro(
        titulo=libro_in.titulo,
        autor=libro_in.autor,
        anio=libro_in.anio,
        descripcion=libro_in.descripcion
    )
    return creado


# Actualizar un libro (PUT)
@app.put("/libros/{id_libro}", response_model=LibroRead)
def actualizar_libro(id_libro: int, libro_upd: LibroUpdate):

    actualizado = gestor.actualizar_libro(
        id_libro=id_libro,
        titulo=libro_upd.titulo,
        autor=libro_upd.autor,
        anio=libro_upd.anio,
        descripcion=libro_upd.descripcion
    )
    if actualizado is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado para actualizar")
    return actualizado


#Eliminar un libro (DELETE)
@app.delete("/libros/{id_libro}", status_code=204)
def eliminar_libro(id_libro: int):

    exito = gestor.eliminar_libro(id_libro)
    if not exito:
        raise HTTPException(status_code=404, detail="Libro no encontrado para eliminar")
    return

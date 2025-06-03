import requests

BASE_URL = "http://127.0.0.1:8000/libros"

def imprimir_respuesta(r):

    print(f"Estado HTTP: {r.status_code}")
    try:
        print("JSON:", r.json())
    except ValueError:
        print("No hay JSON en la respuesta.")
    print("-" * 40)

def main():
    # Listar libros
    print("Listar libros (inicialmente debería estar vacío):")
    resp_get = requests.get(BASE_URL)
    imprimir_respuesta(resp_get)

    # Crear un libro
    print("Crear un libro:")
    datos_nuevo_libro = {
        "titulo": "Cien Años de Soledad",
        "autor": "Gabriel García Márquez",
        "anio": 1967,
        "descripcion": "Novela emblemática del realismo mágico"
    }
    resp_post = requests.post(BASE_URL, json=datos_nuevo_libro)
    imprimir_respuesta(resp_post)

    # Guardamos el ID retornado para usarlo luego
    if resp_post.status_code == 201:
        libro_creado = resp_post.json()
        id_libro = libro_creado["id"]
    else:
        print("No se pudo crear el libro.")
        return

    # Obtener el libro recién creado por ID
    print("Obtener el libro recién creado (GET /libros/{id}):")
    url_individual = f"{BASE_URL}/{id_libro}"
    resp_get_id = requests.get(url_individual)
    imprimir_respuesta(resp_get_id)

    # Actualizar el libro
    print("Actualizar el libro (PUT):")
    datos_actualizacion = {
        "anio": 1970,
    }
    resp_put = requests.put(url_individual, json=datos_actualizacion)
    imprimir_respuesta(resp_put)

    # Mostrar lista de libros otra vez (debería tener el libro actualizado)
    print("Listar libros tras la actualización:")
    resp_get2 = requests.get(BASE_URL)
    imprimir_respuesta(resp_get2)

    # Eliminar el libro (DELETE)
    print("Eliminar el libro (DELETE):")
    resp_delete = requests.delete(url_individual)
    print(f"Estado HTTP: {resp_delete.status_code}")
    print("No esperamos JSON porque devolvemos 204 No Content.")
    print("-" * 40)

    # Intentar obtener de nuevo (GET) para ver que ya no existe
    print("Intentar obtener el libro eliminado (debe dar 404):")
    resp_get3 = requests.get(url_individual)
    imprimir_respuesta(resp_get3)

if __name__ == "__main__":
    main()

def obtener_datos_elemento(tipo: str) -> dict:
    elemento = {}
    elemento['titulo'] = input(f"Ingrese el título del {tipo}: ").strip()
    if tipo == 'libro':
        elemento['autor'] = input("Ingrese el autor: ").strip()
    elif tipo == 'pelicula':
        elemento['director'] = input("Ingrese el director: ").strip()
    elif tipo == 'musica':
        elemento['artista'] = input("Ingrese el artista: ").strip()
    elemento['genero'] = input("Ingrese el género: ").strip()
    valoracion = input("Ingrese la valoración (1-5, opcional): ").strip()
    elemento['valoracion'] = valoracion if valoracion else 'No valorado'
    return elemento

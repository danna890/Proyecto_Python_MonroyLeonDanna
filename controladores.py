from core.coleccion import (
    agregar_elemento,
    listar_elementos,
    buscar_elementos,
    editar_elemento,
    eliminar_elemento,
    obtener_indice_por_titulo
)
from ui.menu import (
    mostrar_menu_agregar,
    mostrar_menu_listar,
    mostrar_menu_buscar,
    mostrar_menu_editar,
    mostrar_menu_eliminar,
    mostrar_menu_categoria,
    mostrar_menu_guardar_cargar
)
from ui.presentacion import mostrar_elementos
from ui.entrada import obtener_datos_elemento
from data.almacenamiento import guardar_coleccion, cargar_coleccion

def manejar_agregar_elemento(coleccion):
    while True:
        mostrar_menu_agregar()
        opcion = input("Selecciona una opción (1-4): ").strip()
        if opcion == '1': tipo = 'libros'
        elif opcion == '2': tipo = 'peliculas'
        elif opcion == '3': tipo = 'musica'
        elif opcion == '4': return
        else:
            print("Opción no válida.")
            continue
        elemento = obtener_datos_elemento(tipo[:-1])
        if agregar_elemento(coleccion, tipo, elemento):
            print(f"\n¡{elemento['titulo']} agregado a {tipo}!")

def manejar_listar_elementos(coleccion):
    while True:
        mostrar_menu_listar()
        opcion = input("Selecciona una opción (1-5): ").strip()
        if opcion == '1':
            mostrar_elementos(listar_elementos(coleccion, 'libros'), 'libros')
        elif opcion == '2':
            mostrar_elementos(listar_elementos(coleccion, 'peliculas'), 'películas')
        elif opcion == '3':
            mostrar_elementos(listar_elementos(coleccion, 'musica'), 'música')
        elif opcion == '4':
            elementos = [e for cat in coleccion.values() for e in cat]
            mostrar_elementos(elementos)
        elif opcion == '5':
            return
        else:
            print("Opción no válida.")

def manejar_buscar_elemento(coleccion):
    while True:
        mostrar_menu_buscar()
        opcion = input("Selecciona una opción (1-4): ").strip()
        if opcion == '1':
            criterio = 'titulo'
        elif opcion == '2':
            criterio = input("Buscar por (autor/director/artista): ").strip().lower()
        elif opcion == '3':
            criterio = 'genero'
        elif opcion == '4':
            return
        else:
            print("Opción no válida.")
            continue
        valor = input(f"Ingrese el {criterio} a buscar: ").strip()
        mostrar_elementos(buscar_elementos(coleccion, criterio, valor),
                          f"búsqueda por {criterio}")

def manejar_editar_elemento(coleccion):
    mostrar_menu_agregar()
    opcion = input("Selecciona tipo (1-4): ").strip()
    if opcion == '4':
        return
    tipo = {'1': 'libros', '2': 'peliculas', '3': 'musica'}.get(opcion)
    if not tipo:
        print("Opción no válida.")
        return
    elementos = listar_elementos(coleccion, tipo)
    if not elementos:
        print(f"No hay {tipo}.")
        return
    mostrar_elementos(elementos, tipo)
    try:
        indice = int(input("Ingrese el número del elemento a editar: ")) - 1
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    mostrar_menu_editar()
    campo_opcion = input("Campo (1-5): ").strip()
    campo = {'1': 'titulo',
             '2': 'autor' if tipo == 'libros' else 'director' if tipo == 'peliculas' else 'artista',
             '3': 'genero',
             '4': 'valoracion'}.get(campo_opcion)
    if not campo:
        return
    nuevo = input(f"Ingrese el nuevo valor de {campo}: ").strip()
    if editar_elemento(coleccion, tipo, indice, campo, nuevo):
        print("Elemento actualizado correctamente.")

def manejar_eliminar_elemento(coleccion):
    mostrar_menu_eliminar()
    opcion = input("Selecciona una opción (1-3): ").strip()
    if opcion == '1':
        tipo = input("Ingrese el tipo (libros/peliculas/musica): ").strip()
        titulo = input("Ingrese el título del elemento a eliminar: ").strip()
        indice = obtener_indice_por_titulo(coleccion, tipo, titulo)
        if indice is not None and eliminar_elemento(coleccion, tipo, indice):
            print("Elemento eliminado correctamente.")
        else:
            print("No se encontró el elemento.")
    elif opcion == '2':
        tipo = input("Ingrese el tipo (libros/peliculas/musica): ").strip()
        elementos = listar_elementos(coleccion, tipo)
        mostrar_elementos(elementos, tipo)
        try:
            indice = int(input("Ingrese el número del elemento a eliminar: ")) - 1
            if eliminar_elemento(coleccion, tipo, indice):
                print("Elemento eliminado correctamente.")
            else:
                print("No se pudo eliminar el elemento.")
        except ValueError:
            print("Número inválido.")
    elif opcion == '3':
        return

def manejar_ver_categoria(coleccion):
    while True:
        mostrar_menu_categoria()
        opcion = input("Selecciona una opción (1-4): ").strip()
        if opcion == '1':
            mostrar_elementos(listar_elementos(coleccion, 'libros'), 'libros')
        elif opcion == '2':
            mostrar_elementos(listar_elementos(coleccion, 'peliculas'), 'películas')
        elif opcion == '3':
            mostrar_elementos(listar_elementos(coleccion, 'musica'), 'música')
        elif opcion == '4':
            return

def manejar_guardar_cargar(coleccion):
    while True:
        mostrar_menu_guardar_cargar()
        opcion = input("Selecciona una opción (1-3): ").strip()
        if opcion == '1':
            guardar_coleccion(coleccion)
            print("Colección guardada.")
        elif opcion == '2':
            archivo = input("Archivo a cargar (Enter = colecciones.json): ").strip() or 'colecciones.json'
            coleccion.update(cargar_coleccion(archivo))
            print("Colección cargada.")
        elif opcion == '3':
            return
        else:
            print("Opción no válida.")
from coleccion import cargar_coleccion, guardar_coleccion
from menu_consola import (
    mostrar_menu_principal,
    mostrar_menu_agregar,
    mostrar_menu_listar,
    mostrar_menu_buscar,
    mostrar_menu_editar,
    mostrar_menu_eliminar,
    mostrar_menu_categoria,
    mostrar_menu_guardar_cargar,
    mostrar_elementos,
    obtener_datos_elemento
)
from coleccion import (
    agregar_elemento,
    listar_elementos,
    buscar_elementos,
    editar_elemento,
    eliminar_elemento,
    obtener_indice_por_titulo
)



def main():
    coleccion = cargar_coleccion()
    
    while True:
        mostrar_menu_principal()
        opcion = input("Selecciona una opción (1-8): ").strip()
        if opcion == '1':
            manejar_agregar_elemento(coleccion)
        elif opcion == '2':
            manejar_listar_elementos(coleccion)
        elif opcion == '3':
            manejar_buscar_elemento(coleccion)
        elif opcion == '4':
            manejar_editar_elemento(coleccion)
        elif opcion == '5':
            manejar_eliminar_elemento(coleccion)
        elif opcion == '6':
            manejar_ver_categoria(coleccion)
        elif opcion == '7':
            manejar_guardar_cargar(coleccion)
        elif opcion == '8':
            guardar_coleccion(coleccion)
            print("¡Gracias por usar el Administrador de Colección!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 8.")

def manejar_agregar_elemento(coleccion):
    """Maneja la lógica para agregar nuevos elementos"""
    while True:
        mostrar_menu_agregar()
        opcion = input("Selecciona una opción (1-4): ").strip()
        
        if opcion == '1':  
            tipo = 'libros'
        elif opcion == '2': 
            tipo = 'peliculas'
        elif opcion == '3':  
            tipo = 'musica'
        elif opcion == '4':  
            return
        else:
            print("Opción no válida.")
            continue
        
        elemento = obtener_datos_elemento(tipo[:-1]) 
        if agregar_elemento(coleccion, tipo, elemento):
            print(f"\n¡{elemento['titulo']} ha sido agregado a la colección de {tipo}!")
        else:
            print("\nError al agregar el elemento.")

def manejar_listar_elementos(coleccion):
    while True:
        mostrar_menu_listar()
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == '1': 
            elementos = listar_elementos(coleccion, 'libros')
            mostrar_elementos(elementos, 'libros')
        elif opcion == '2':
            elementos = listar_elementos(coleccion, 'peliculas')
            mostrar_elementos(elementos, 'películas')
        elif opcion == '3': 
            elementos = listar_elementos(coleccion, 'musica')
            mostrar_elementos(elementos, 'música')
        elif opcion == '4': 
            elementos = []
            for cat in coleccion.values():
                elementos.extend(cat)
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
        resultados = buscar_elementos(coleccion, criterio, valor)
        mostrar_elementos(resultados, f"resultados de búsqueda por {criterio}")

def manejar_editar_elemento(coleccion):
    print("\nSeleccione el tipo de elemento a editar:")
    mostrar_menu_agregar()
    opcion_tipo = input("Selecciona una opción (1-4): ").strip()
    
    if opcion_tipo == '4':
        return
    
    if opcion_tipo == '1':
        tipo = 'libros'
    elif opcion_tipo == '2':
        tipo = 'peliculas'
    elif opcion_tipo == '3':
        tipo = 'musica'
    else:
        print("Opción no válida.")
        return
    
    
    elementos = listar_elementos(coleccion, tipo)
    if not elementos:
        print(f"No hay {tipo} en la colección.")
        return
    
    mostrar_elementos(elementos, tipo)
    try:
        indice = int(input("Ingrese el número del elemento a editar: ")) - 1
        if indice < 0 or indice >= len(elementos):
            print("Número de elemento inválido.")
            return
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    
    while True:
        mostrar_menu_editar()
        opcion_campo = input("Selecciona una opción (1-5): ").strip()
        
        if opcion_campo == '1': 
            campo = 'titulo'
        elif opcion_campo == '2': 
            if tipo == 'libros':
                campo = 'autor'
            elif tipo == 'peliculas':
                campo = 'director'
            else:
                campo = 'artista'
        elif opcion_campo == '3':
            campo = 'genero'
        elif opcion_campo == '4': 
            campo = 'valoracion'
        elif opcion_campo == '5':  
            return
        else:
            print("Opción no válida.")
            continue
        
        nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ").strip()
        if editar_elemento(coleccion, tipo, indice, campo, nuevo_valor):
            print("¡Elemento actualizado correctamente!")
        else:
            print("Error al actualizar el elemento.")
        return

def manejar_eliminar_elemento(coleccion):

    while True:
        mostrar_menu_eliminar()
        opcion = input("Selecciona una opción (1-3): ").strip()
        
        if opcion == '1':  
            tipo = input("Ingrese el tipo (libros/peliculas/musica): ").strip()
            if tipo not in ['libros', 'peliculas', 'musica']:
                print("Tipo no válido.")
                continue
            
            titulo = input("Ingrese el título del elemento a eliminar: ").strip()
            indice = obtener_indice_por_titulo(coleccion, tipo, titulo)
            
            if indice is not None:
                elemento = coleccion[tipo][indice]
                confirmar = input(f"¿Está seguro de eliminar '{elemento['titulo']}'? (Si/No): ").lower()
                if confirmar == 'Si':
                    if eliminar_elemento(coleccion, tipo, indice):
                        print("Elemento eliminado correctamente.")
                    else:
                        print("Error al eliminar el elemento.")
                else:
                    print("Eliminación cancelada.")
            else:
                print("No se encontró el elemento con ese título.")
        
        elif opcion == '2':  
            tipo = input("Ingrese el tipo (libros/peliculas/musica): ").strip()
            if tipo not in ['libros', 'peliculas', 'musica']:
                print("Tipo no válido.")
                continue
            
            elementos = listar_elementos(coleccion, tipo)
            mostrar_elementos(elementos, tipo)
            
            try:
                indice = int(input("Ingrese el número del elemento a eliminar: ")) - 1
                if 0 <= indice < len(elementos):
                    elemento = elementos[indice]
                    confirmar = input(f"¿Está seguro de eliminar '{elemento['titulo']}'? (Si/No): ").lower()
                    if confirmar == 'Si':
                        if eliminar_elemento(coleccion, tipo, indice):
                            print("Elemento eliminado correctamente.")
                        else:
                            print("Error al eliminar el elemento.")
                    else:
                        print("Eliminación cancelada.")
                else:
                    print("Número de elemento inválido.")
            except ValueError:
                print("Debe ingresar un número válido.")
        
        elif opcion == '3':  
            return
        else:
            print("Opción no válida.")

def manejar_ver_categoria(coleccion):
    
    while True:
        mostrar_menu_categoria()
        opcion = input("Selecciona una opción (1-4): ").strip()
        
        if opcion == '1':  
            elementos = listar_elementos(coleccion, 'libros')
            mostrar_elementos(elementos, 'libros')
        elif opcion == '2': 
            elementos = listar_elementos(coleccion, 'peliculas')
            mostrar_elementos(elementos, 'películas')
        elif opcion == '3': 
            elementos = listar_elementos(coleccion, 'musica')
            mostrar_elementos(elementos, 'música')
        elif opcion == '4':  
            return
        else:
            print("Opción no válida.")

def manejar_guardar_cargar(coleccion):
    
    while True:
        mostrar_menu_guardar_cargar()
        opcion = input("Selecciona una opción (1-3): ").strip()
        
        if opcion == '1':  
            guardar_coleccion(coleccion)
            print("Colección guardada correctamente.")
        elif opcion == '2': 
            archivo = input("Ingrese el nombre del archivo a cargar (deje vacío para coleccion.json): ").strip() or 'coleccion.json'
            try:
                nueva_coleccion = cargar_coleccion(archivo)
                coleccion.update(nueva_coleccion)
                print("Colección cargada correctamente.")
            except Exception as e:
                print(f"Error al cargar la colección: {e}")
        elif opcion == '3': 
            return
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
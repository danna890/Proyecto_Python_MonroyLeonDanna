"""
Módulo para mostrar los menús y manejar la interacción con el usuario
"""

from typing import List, Dict

def mostrar_menu_principal():
    print("""
    ===========================================
            Administrador de Colección
    ===========================================
    1. Añadir un Nuevo Elemento
    2. Ver Todos los Elementos
    3. Buscar un Elemento
    4. Editar un Elemento
    5. Eliminar un Elemento
    6. Ver Elementos por Categoría
    7. Guardar y Cargar Colección
    8. Salir
    ===========================================
    """)

def mostrar_menu_agregar():
    """Muestra el menú para agregar elementos"""
    print("""
    ===========================================
            Añadir un Nuevo Elemento
    ===========================================
    ¿Qué tipo de elemento deseas añadir?
    1. Libro
    2. Película
    3. Música
    4. Regresar al Menú Principal
    ===========================================
    """)

def mostrar_menu_listar():
    """Muestra el menú para listar elementos"""
    print("""
    ===========================================
            Ver Todos los Elementos
    ===========================================
    ¿Qué categoría deseas ver?
    1. Ver Todos los Libros
    2. Ver Todas las Películas
    3. Ver Toda la Música
    4. Ver Todo
    5. Regresar al Menú Principal
    ===========================================
    """)

def mostrar_menu_buscar():
    """Muestra el menú para buscar elementos"""
    print("""
    ===========================================
            Buscar un Elemento
    ===========================================
    ¿Cómo deseas buscar?
    1. Buscar por Título
    2. Buscar por Autor/Director/Artista
    3. Buscar por Género
    4. Regresar al Menú Principal
    ===========================================
    """)

def mostrar_menu_editar():
    """Muestra el menú para editar elementos"""
    print("""
    ===========================================
            Editar un Elemento
    ===========================================
    ¿Qué tipo de cambio deseas realizar?
    1. Editar Título
    2. Editar Autor/Director/Artista
    3. Editar Género
    4. Editar Valoración
    5. Regresar al Menú Principal
    ===========================================
    """)

def mostrar_menu_eliminar():
    """Muestra el menú para eliminar elementos"""
    print("""
    ===========================================
            Eliminar un Elemento
    ===========================================
    ¿Cómo deseas eliminar?
    1. Eliminar por Título
    2. Eliminar por Identificador Único
    3. Regresar al Menú Principal
    ===========================================
    """)

def mostrar_menu_categoria():
    """Muestra el menú para ver por categoría"""
    print("""
    ===========================================
            Ver Elementos por Categoría
    ===========================================
    ¿Qué categoría deseas ver?
    1. Ver Libros
    2. Ver Películas
    3. Ver Música
    4. Regresar al Menú Principal
    ===========================================
    """)

def mostrar_menu_guardar_cargar():
    """Muestra el menú para guardar/cargar colección"""
    print("""
    ===========================================
            Guardar y Cargar Colección
    ===========================================
    ¿Qué deseas hacer?
    1. Guardar la Colección Actual
    2. Cargar una Colección Guardada
    3. Regresar al Menú Principal
    ===========================================
    """)

def mostrar_elementos(elementos: List[Dict], tipo: str = ''):
    if not elementos:
        print(f"No hay {tipo} en la colección." if tipo else "La colección está vacía.")
        return
    
    print(f"\n{'='*30}")
    print(f"        {tipo.upper() if tipo else 'TODOS LOS ELEMENTOS'}")
    print(f"{'='*30}")
    
    for i, elemento in enumerate(elementos, 1):
        print(f"\nElemento #{i}")
        for clave, valor in elemento.items():
            print(f"{clave.capitalize()}: {valor}")
    
    print(f"\nTotal: {len(elementos)} elementos")

def obtener_datos_elemento(tipo: str) -> Dict:
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
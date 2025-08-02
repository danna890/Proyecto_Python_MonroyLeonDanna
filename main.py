from data.almacenamiento import cargar_coleccion, guardar_coleccion
from ui.menu import mostrar_menu_principal
from controladores import (
    manejar_agregar_elemento,
    manejar_listar_elementos,
    manejar_buscar_elemento,
    manejar_editar_elemento,
    manejar_eliminar_elemento,
    manejar_ver_categoria,
    manejar_guardar_cargar
)

def main():
    coleccion = cargar_coleccion()
    while True:
        mostrar_menu_principal()
        opcion = input("Selecciona una opción (1-8): ").strip()
        if opcion == '1': manejar_agregar_elemento(coleccion)
        elif opcion == '2': manejar_listar_elementos(coleccion)
        elif opcion == '3': manejar_buscar_elemento(coleccion)
        elif opcion == '4': manejar_editar_elemento(coleccion)
        elif opcion == '5': manejar_eliminar_elemento(coleccion)
        elif opcion == '6': manejar_ver_categoria(coleccion)
        elif opcion == '7': manejar_guardar_cargar(coleccion)
        elif opcion == '8':
            guardar_coleccion(coleccion)
            print("¡Gracias por usar el Administrador de Colección!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()

from typing import List, Dict

def mostrar_elementos(elementos: List[Dict], tipo: str = ''):
    if not elementos:
        print(f"No hay {tipo} en la colección." if tipo else "Colección vacía.")
        return
    print(f"\n{'='*30}")
    print(f"        {tipo.upper() if tipo else 'TODOS LOS ELEMENTOS'}")
    print(f"{'='*30}")
    for i, elemento in enumerate(elementos, 1):
        print(f"\nElemento #{i}")
        for clave, valor in elemento.items():
            print(f"{clave.capitalize()}: {valor}")
    print(f"\nTotal: {len(elementos)} elementos")

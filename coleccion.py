import json
from typing import Dict, List, Optional, Union

def cargar_coleccion(nombre_archivo: str = 'coleccion.json') -> Dict[str, List[Dict]]:
    try:
        with open(nombre_archivo, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {'libros': [], 'peliculas': [], 'musica': []}
    except json.JSONDecodeError:
        return {'libros': [], 'peliculas': [], 'musica': []}

def guardar_coleccion(coleccion: Dict[str, List[Dict]], nombre_archivo: str = 'coleccion.json'):
    """
    Guarda la colección en un archivo JSON
    """
    
    with open(nombre_archivo, 'w') as archivo:
        json.dump(coleccion, archivo, ensure_ascii=False)

def agregar_elemento(coleccion: Dict[str, List[Dict]], tipo: str, elemento: Dict) -> bool:
    """
    Agrega un nuevo elemento a la colección
    """
    
    if tipo in coleccion:
        coleccion[tipo].append(elemento)
        return True
    return False

def listar_elementos(coleccion: Dict[str, List[Dict]], tipo: Optional[str] = None) -> Union[Dict[str, List[Dict]], List[Dict]]:
    """
    Lista elementos de la colección, opcionalmente filtrados por tipo
    """
    
    if tipo:
        return coleccion.get(tipo, [])
    return coleccion

def buscar_elementos(coleccion: Dict[str, List[Dict]], criterio: str, valor: str) -> List[Dict]:
    """
    Busca elementos en la colección según un criterio
    """
    
    resultados = []
    for categoria in coleccion.values():
        for elemento in categoria:
            if valor.lower() in str(elemento.get(criterio, '')).lower():
                resultados.append(elemento)
    return resultados

def editar_elemento(coleccion: Dict[str, List[Dict]], tipo: str, indice: int, campo: str, nuevo_valor: str) -> bool:
    """
    Edita un elemento existente en la colección
    """
    
    try:
        coleccion[tipo][indice][campo] = nuevo_valor
        return True
    except (KeyError, IndexError):
        return False

def eliminar_elemento(coleccion: Dict[str, List[Dict]], tipo: str, indice: int) -> bool:
    """
    Elimina un elemento de la colección
    """
    
    try:
        coleccion[tipo].pop(indice)
        return True
    except (KeyError, IndexError):
        return False

def obtener_indice_por_titulo(coleccion: Dict[str, List[Dict]], tipo: str, titulo: str) -> Optional[int]:
    for i, elemento in enumerate(coleccion.get(tipo, [])):
        if elemento.get('titulo', '').lower() == titulo.lower():
            return i
    return None
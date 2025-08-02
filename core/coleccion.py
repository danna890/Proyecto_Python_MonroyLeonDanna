import json
from typing import Dict, List, Optional, Union

def cargar_coleccion(nombre_archivo: str = 'colecciones.json') -> Dict[str, List[Dict]]:
    try:
        with open(nombre_archivo, 'r') as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {'libros': [], 'peliculas': [], 'musica': []}

def guardar_coleccion(coleccion: Dict[str, List[Dict]], nombre_archivo: str = 'colecciones.json'):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(coleccion, archivo, ensure_ascii=False, indent=4)

def agregar_elemento(coleccion: Dict[str, List[Dict]], tipo: str, elemento: Dict) -> bool:
    if tipo in coleccion:
        coleccion[tipo].append(elemento)
        return True
    return False

def listar_elementos(coleccion: Dict[str, List[Dict]], tipo: Optional[str] = None) -> Union[Dict[str, List[Dict]], List[Dict]]:
    return coleccion.get(tipo, []) if tipo else coleccion

def buscar_elementos(coleccion: Dict[str, List[Dict]], criterio: str, valor: str) -> List[Dict]:
    resultados = []
    for categoria in coleccion.values():
        for elemento in categoria:
            if valor.lower() in str(elemento.get(criterio, '')).lower():
                resultados.append(elemento)
    return resultados

def editar_elemento(coleccion: Dict[str, List[Dict]], tipo: str, indice: int, campo: str, nuevo_valor: str) -> bool:
    try:
        coleccion[tipo][indice][campo] = nuevo_valor
        return True
    except (KeyError, IndexError):
        return False

def eliminar_elemento(coleccion: Dict[str, List[Dict]], tipo: str, indice: int) -> bool:
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

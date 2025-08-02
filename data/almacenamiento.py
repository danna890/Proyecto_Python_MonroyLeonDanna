import json
from typing import Dict, List

def cargar_coleccion(nombre_archivo: str = 'colecciones.json') -> Dict[str, List[Dict]]:
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return {'libros': [], 'peliculas': [], 'musica': []}

def guardar_coleccion(coleccion: Dict[str, List[Dict]], nombre_archivo: str = 'colecciones.json'):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(coleccion, archivo, ensure_ascii=False, indent=4)

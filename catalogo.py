"""Lectura del catálogo de satélites, grupos y lanzamientos por año."""
import json

GRUPOS = {
    "STARLINK": "Starlink",
    "ONEWEB": "OneWeb",
    "KUIPER": "Kuiper",
    "QIANFAN": "Qianfan",
    "IRIDIUM": "Iridium",
    "GLOBALSTAR": "Globalstar",
    "NAVSTAR": "GPS",
    "BEIDOU": "BeiDou",
}

def leer_satelites(ruta):
    """Lee el archivo JSON (utf-8) y devuelve la lista de registros.
        
    Si el archivo no existe, emite un aviso y devuelve una lista vacia"""

    try:
        with open(ruta, encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Aviso: no se encontro el archivo '{ruta}'.")
        return []

def anio_lanzamiento(registro):
    """Devuelve el año de lanzamiento (int) a partir de OBJECT_ID"""
    return int(registro['OBJECT_ID'][:4])

def grupo(nombre):
    """Devuelve el grupo según el prefijo del nombre, o 'Otros'."""
    for prefijo, nombre_grupo in GRUPOS.items():
        if nombre.startswith(prefijo):
            return nombre_grupo
    return "Otros"

def contar_por_grupo(registros):
    """Devuelve {grupo: cantidad de satélites}."""
    conteo = {}
    for registro in registros:
        g = grupo(registro["OBJECT_NAME"])
        conteo[g] = conteo.get(g, 0) + 1
    return conteo

def lanzamientos_por_anio(registros):
    """Devuelve {año: cantidad de satélites lanzados ese año}."""
    conteo = {}
    for registro in registros:
        anio = anio_lanzamiento(registro)
        conteo[anio] = conteo.get(anio, 0) + 1
    return conteo

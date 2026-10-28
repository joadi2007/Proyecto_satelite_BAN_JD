from catalogo import grupo

def contar_por_tipo(satelites) -> dict:
    '''Devuelve un diccionario {"LEO": n, "MEO": n, "GEO": n, "HEO": n},
    con las cuatro claves siempre presentes (en 0 si no hay satélites de ese tipo).'''


def mas_bajo(satelites) -> str:
    '''Devuelve el objeto Satelite de menor altitud.'''

def mas_alto(satelites) -> str:
    '''Devuelve el objeto Satelite de mayor altitud.'''

def en_zona(satelites, zona) -> list:
    '''Devuelve una lista de los satélites dentro de la zona (usando el método esta_en_zona).'''

def ordenar_por(satelites, atributo, descendente=False) -> list:
    '''Función genérica que devuelve una lista nueva ordenada por
    cualquier atributo ("altitud_km", "latitud", "nombre", ...).'''

def top_n(satelites, n, mas_altos=True) -> int:
    '''Devuelve los n satélites más altos (o más bajos), reutilizando ordenar_por.'''

def resumen_por_grupo(satelites) -> dict:
    '''Usando grupo de catalogo.py, devuelve un diccionario con un resumen de las altitudes de cada grupo.'''

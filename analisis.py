from catalogo import grupo

def contar_por_tipo(satelites) -> dict:
    '''Devuelve un diccionario {"LEO": n, "MEO": n, "GEO": n, "HEO": n},
    con las cuatro claves siempre presentes (en 0 si no hay satélites de ese tipo).'''
    
    conteo = {'LEO': 0, 'MEO': 0, 'GEO': 0, 'HEO': 0}
    for sat in satelites:
        tipo = sat.tipo_orbita()
        if tipo in conteo:
            conteo[tipo] += 1
    return conteo


def mas_bajo(satelites):
    '''Devuelve el objeto Satelite de menor altitud.'''
    
    if not satelites:
        return None
    return min(satelites, key=lambda sat: sat.altitud_km)


def mas_alto(satelites):
    '''Devuelve el objeto Satelite de mayor altitud.'''
    
    if not satelites:
        return None
    return max(satelites, key=lambda sat: sat.altitud_km)


def en_zona(satelites, zona) -> list:
    '''Devuelve una lista de los satélites dentro de la zona.'''
    
    return [sat for sat in satelites if sat.esta_en_zona(zona)]


def ordenar_por(satelites, atributo, descendente=False) -> list:
    '''Función genérica que devuelve una lista nueva ordenada por
    cualquier atributo ("altitud_km", "latitud", "nombre", ...).'''
    
    return sorted(satelites, key=lambda sat: getattr(sat, atributo), reverse=descendente)


def top_n(satelites, n, mas_altos=True) -> list:
    '''Devuelve los n satélites más altos (o más bajos), reutilizando ordenar_por.'''
    
    ordenados = ordenar_por(satelites, 'altitud_km', descendente=mas_altos)
    return ordenados[:n]


def resumen_por_grupo(satelites) -> dict:
    '''Usando grupo de catalogo.py, devuelve un diccionario con un resumen de las altitudes de cada grupo.'''
    agrupados = {}

    for sat in satelites:
        g = grupo(sat.nombre)
        if g not in agrupados:
            agrupados[g] = []
        agrupados[g].append(sat.altitud_km)
    
    resumen = {}
    for g, altitudes in agrupados.items():
        resumen[g] = {
            'cantidad': len(altitudes),
            'min': min(altitudes),
            'max': max(altitudes),
            'promedio': sum(altitudes) / len(altitudes)
        }
    return resumen
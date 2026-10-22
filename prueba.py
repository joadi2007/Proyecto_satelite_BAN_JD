from catalogo import leer_satelites, grupo, contar_por_grupo, lanzamientos_por_anio

registros = leer_satelites("datos/satelites.json")

print(len(registros))                       # 16710
print(grupo("STARLINK-1234"))               # Starlink
print(grupo("ISS (ZARYA)"))                 # Otros

conteo = contar_por_grupo(registros)
print(conteo)
print(sum(conteo.values()))                 # tiene que dar 16710

print(lanzamientos_por_anio(registros)[2025])
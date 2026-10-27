from datetime import datetime, timezone

from catalogo import leer_satelites, grupo, contar_por_grupo, lanzamientos_por_anio
from satelite import Satelite, crear_satelites

# --- Pruebas de catalogo.py ---
registros = leer_satelites("datos/satelites.json")

print(len(registros))                           # 16710
print(grupo("STARLINK-1234"))                   # Starlink
print(grupo("ISS (ZARYA)"))                     # Otros

conteo = contar_por_grupo(registros)
print(conteo)
print(sum(conteo.values()))                     # 16710

print(lanzamientos_por_anio(registros)[2025])   # 4289

# --- Pruebas de la clase Satelite ---
iss = Satelite("ISS (ZARYA)", -41.0, -71.0, 419.7)
print(iss)                                      # ISS (ZARYA) | LEO | 419.7 km
print(iss.tipo_orbita())                        # LEO
print(Satelite("A", 0, 0, 2000).tipo_orbita())  # MEO
print(Satelite("B", 0, 0, 36000).tipo_orbita()) # GEO
print(Satelite("C", 0, 0, 40000).tipo_orbita()) # HEO

BARILOCHE = (-76.30, -46.13, -66.30, -36.13)
print(iss.esta_en_zona(BARILOCHE))                                  # True
print(Satelite("D", 0, 0, 500).esta_en_zona(BARILOCHE))             # False
print(Satelite("E", -36.13, -66.30, 500).esta_en_zona(BARILOCHE))   # True (borde)

# --- Prueba de crear_satelites (tarda unos segundos) ---
sats = crear_satelites(registros, datetime.now(timezone.utc))
print(len(registros), len(sats))                # 16710 y unos pocos menos (~16707)
print(sats[0])

# Ningún satélite creado puede tener altitud menor a 100 km ni NaN
print(all(s.altitud_km >= 100 for s in sats))   # True
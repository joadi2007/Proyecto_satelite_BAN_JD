from funciones_base import crear_objeto_skyfield, obtener_posicion

class Satelite:
    def __init__(self, nombre, latitud, longitud, altitud_km):
        """Guarda los cuatro datos como atributos del objeto."""
    self.nombre = nombre
    self.latitud = latitud
    self.longitud = longitud
    self.altitud_km = altitud_km

    def tipo_orbita(self):
        """Devuelve "LEO", "MEO", "GEO" o "HEO" según la altitud (ver tabla)."""
        if self.altitud_km < 2000:
            return 'LEO'
        elif self.altitud_km < 34000:
            return 'MEO'
        elif self.altitud_km <= 37000:
            return 'GEO'       
        else:
            return 'HEO'

    def esta_en_zona(self, zona):
        """True si el satélite está dentro de la zona (lon_min, lat_min, lon_max, lat_max)."""
        lon_min, lat_min, lon_max, lat_max = zona
        return (lon_min <= self.longitud <= lon_max) and (lat_min <= self.latitud <= lat_max)
    
    def __str__(self):
        """Por ejemplo: 'ISS (ZARYA) | LEO | 419.7 km'"""
        tipo = self.tipo_orbita()
        return f'{self.nombre} | {tipo} | {self.altitud_km:.1f} km'
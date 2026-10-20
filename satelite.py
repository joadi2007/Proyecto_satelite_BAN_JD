class Satelite:
    def __init__(self, nombre, latitud, longitud, altitud_km):
        """Guarda los cuatro datos como atributos del objeto."""

    def tipo_orbita(self):
        """Devuelve "LEO", "MEO", "GEO" o "HEO" según la altitud (ver tabla)."""

    def esta_en_zona(self, zona):
        """True si el satélite está dentro de la zona (lon_min, lat_min, lon_max, lat_max)."""

    def __str__(self):
        """Por ejemplo: 'ISS (ZARYA) | LEO | 419.7 km'"""


def crear_satelites(registros, momento):
    """Devuelve una lista de objetos Satelite con su posición en `momento`."""
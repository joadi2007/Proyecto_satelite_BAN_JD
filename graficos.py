import matplotlib.pyplot as plt
import numpy as np
from catalogo import anio_lanzamiento
from matplotlib.patches import Circle

def barras_lanzamientos(por_anio, desde=1990, hasta=2026):
    """Barras con la cantidad de satélites lanzados por año.

    por_anio: diccionario {año: cantidad}, como devuelve lanzamientos_por_anio.
    Los años sin datos cuentan como 0.
    """
    anios = list(range(desde, hasta + 1))
    cantidades = [por_anio.get(a, 0) for a in anios]

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(anios, cantidades)
    ax.set_xlabel("Año de lanzamiento")
    ax.set_ylabel("Satélites lanzados")
    ax.set_title("Lanzamientos por año (satélites activos hoy)")
    plt.close(fig)
    return fig

def barras_apiladas(datos_abajo, datos_arriba, etiqueta_abajo, etiqueta_arriba,
                    desde=1990, hasta= 2026):
    """Barras apiladas por año con dos series {año: cantidad}.

    Los años que faltan en alguno de los diccionarios cuentan como 0.
    """
    anios = list(range(desde, hasta + 1))
    abajo = [datos_abajo.get(a, 0) for a in anios]
    arriba = [datos_arriba.get(a, 0) for a in anios]

    fig , ax = plt.subplots(figsize= (10, 4))
    ax.bar(anios, abajo, label=etiqueta_abajo)
    ax.bar(anios, arriba, bottom=abajo, label=etiqueta_arriba)
    ax.set_xlabel('Año de lanzamiento')
    ax.set_ylabel('Satélites lanzados')
    ax.set_title(f'Lanzamientos por año: {etiqueta_abajo} y {etiqueta_arriba}')
    ax.legend()
    plt.close(fig)

    return fig

def barras_altura_media(resumen):
    """Barras con la altitud media de cada grupo.

    resumen: diccionario que devuelve resumen_por_grupo.
    Los grupos se ordenan de menor a mayor altitud media.
    """
    ordenados = sorted(resumen.items(), key=lambda par: par[1]['media'])
    grupos = [g for g, _ in ordenados]
    medias = [datos['media'] for _, datos in ordenados]

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(grupos, medias)
    ax.axhline(2000, color='gray', linestyle='--', label='Limite LEO (2.000 km)')
    ax.set_xlabel('Grupo')
    ax.set_ylabel('Altitud media (km)')    
    ax.set_title('Altitud medio por grupo')   
    ax.legend()
    plt.close(fig)

    return fig 

def hist_leo(satelites, ancho_bin=10):
    '''Histograma de altitudes en órbita baja (entre 200 y 2000 km) con el ancho de bin indicado.'''

    altitudes = [s.altitud_km for s in satelites if 200 <= s.altitud_km <= 2000]
    bins = np.arange(200, 2000 + ancho_bin, ancho_bin)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.hist(altitudes, bins=bins, edgecolor="k")
    ax.set_xlabel("Altitud (km)")
    ax.set_ylabel("Cantidad de satélites")
    ax.set_title(f"Altitudes en órbita baja (bins de {ancho_bin} km)")
    plt.close(fig)
    return fig

def hist_alt_log(satelites, n_bins=50):
    '''Histograma de todas las altitudes con eje X en escala logarítmica y bins de ancho logarítmico.'''
    altitudes = [s.altitud_km for s in satelites if s.altitud_km > 0]
    bins = np.logspace(np.log10(min(altitudes)), np.log10(max(altitudes)), 50)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.hist(altitudes, bins=bins, edgecolor="k")
    ax.set_xscale("log")
    ax.set_xlabel("Altitud (km, escala logarítmica)")
    ax.set_ylabel("Cantidad de satélites")
    ax.set_title(f"Altitudes de todos los satélites ({n_bins} bins logarítmicos)")
    plt.close(fig)
    return fig

def hist_inc(registros):
    '''Histograma de la inclinación orbital (de 0° a 180°) con bins de 1° a partir de los registros JSON.'''
    inclinaciones = [float(reg['INCLINATION']) for reg in registros if 'INCLINATION' in reg]
    bins = np.arange(0, 181, 1)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.hist(inclinaciones, bins=bins, edgecolor="k")
    ax.set_xlim(0, 180)
    ax.set_xlabel("Inclinación (grados)")
    ax.set_ylabel("Cantidad de satélites")
    ax.set_title("Distribución de inclinaciones orbitales")
    plt.close(fig)
    return fig


# tema libre
def evo_orbitas(registros, satelites):
    """Evolución de la cantidad de satélites por tipo de órbita según el año de lanzamiento.

    registros: lista de diccionarios del JSON (de ahí sale el año de lanzamiento).
    satelites: lista de objetos Satelite (de ahí sale el tipo de órbita).
    """
    anio_por_nombre = {r["OBJECT_NAME"]: anio_lanzamiento(r) for r in registros}

    datos = {}
    for s in satelites:
        anio = anio_por_nombre[s.nombre]
        tipo = s.tipo_orbita()
        if anio not in datos:
            datos[anio] = {"LEO": 0, "MEO": 0, "GEO": 0, "HEO": 0}
        datos[anio][tipo] += 1
    anios = sorted(datos)

    fig, ax = plt.subplots(figsize=(10, 4))
    for tipo, color in (("LEO", "blue"), ("MEO", "orange"), ("GEO", "green")):
        ax.plot(anios, [datos[a][tipo] for a in anios], label=tipo, color=color)
    ax.set_yscale("symlog")
    ax.set_xlabel("Año de lanzamiento")
    ax.set_ylabel("Cantidad de satélites")
    ax.set_title("Evolución de satélites por tipo de órbita")
    ax.legend()
    plt.close(fig)
    return fig

RADIO_TIERRA = 6371  # km
# (tipo, altitud mínima, altitud máxima, color); HEO se dibuja hasta el borde del gráfico
BANDAS = [("LEO", 0, 2000, "#b7d4f0"), ("MEO", 2000, 34000, "#fde3b8"),
          ("GEO", 34000, 37000, "#b9e3c0"), ("HEO", 37000, 1e9, "#f5c6cb")]


def esquema_orbitas(registros, satelites, anio, solo_ese_anio=False):
    """Esquema de las órbitas alrededor de la Tierra con los satélites lanzados hasta un año.

    registros: lista de diccionarios del JSON (de ahí sale el año de lanzamiento).
    satelites: lista de objetos Satelite (de ahí sale la altitud).
    anio: año hasta el cual se cuentan los satélites lanzados.
    solo_ese_anio: si es True, se cuentan solo los lanzados en ese año.
    Los satélites están dispuestos en ángulos al azar: lo que importa es su altitud.
    """
    anio_por_nombre = {r["OBJECT_NAME"]: anio_lanzamiento(r) for r in registros}
    if solo_ese_anio:
        elegidos = [s for s in satelites if anio_por_nombre[s.nombre] == anio]
    else:
        elegidos = [s for s in satelites if anio_por_nombre[s.nombre] <= anio]

    conteo = {tipo: 0 for tipo, _, _, _ in BANDAS}
    for s in elegidos:
        conteo[s.tipo_orbita()] += 1

    rng = np.random.default_rng(0)
    radios = np.array([RADIO_TIERRA + s.altitud_km for s in elegidos])
    angulos = rng.uniform(0, 2 * np.pi, len(radios))

    fig, ejes = plt.subplots(1, 2, figsize=(12, 6))
    for ax, limite, titulo in ((ejes[0], 50000, "Escala real"),
                               (ejes[1], RADIO_TIERRA + 2200, "Zoom en órbita baja")):
        for tipo, minimo, maximo, color in reversed(BANDAS):   # de afuera hacia adentro
            ax.add_patch(Circle((0, 0), RADIO_TIERRA + min(maximo, 1e6), color=color))
        ax.add_patch(Circle((0, 0), RADIO_TIERRA, color="tab:cyan"))
        dentro = radios <= limite
        ax.scatter(radios[dentro] * np.cos(angulos[dentro]), radios[dentro] * np.sin(angulos[dentro]),
                   s=2, color="k")
        ax.set_xlim(-limite, limite)
        ax.set_ylim(-limite, limite)
        ax.set_aspect("equal")
        ax.set_title(titulo)
        ax.set_xlabel("km")
    detalle = "solo lanzados en" if solo_ese_anio else "lanzados hasta"
    ejes[0].text(0.02, 0.02, "\n".join(f"{t}: {n}" for t, n in conteo.items()),
                 transform=ejes[0].transAxes, fontsize=9)
    fig.suptitle(f"Satélites {detalle} {anio}")
    plt.close(fig)
    return fig
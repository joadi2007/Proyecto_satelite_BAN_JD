import matplotlib.pyplot as plt
import numpy as np

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
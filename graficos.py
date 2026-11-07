import matplotlib.pyplot as plt

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

def altitud_media(resumen: dict):
    '''Gráfico de barras con la altitud media de cada grupo a partir de resumen_por_grupo.'''

    grupos = list(resumen.keys())
    medias = [resumen[g]['media'] for g in grupos]

    plt.figure(figsize=(10, 4))
    plt.bar(grupos, medias)
    plt.xlabel('Grupo')
    plt.ylabel('Grupo')
    plt.title('Altitud media por grupo')
    plt.show()
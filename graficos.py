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
    ax.set_ylabel('Satelites lanzados')
    ax.set_title(f'lanzamientos por año: {etiqueta_abajo} y {etiqueta_arriba}')
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
    ax.legend()
    plt.close(fig)

    return fig 

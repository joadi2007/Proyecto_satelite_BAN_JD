# Proyecto_satelite_BAN_JD

Trabajo Práctico de Programación 1 (Etapas 1 y 2): seguimiento y caracterización de satélites.
El proyecto lee un catálogo de satélites (CelesTrak), calcula su posición con Skyfield,
genera estadísticas (conteo por grupo y por tipo de órbita, lanzamientos por año,
altitudes por grupo, satélites sobre Bariloche) y las muestra en gráficos con Matplotlib.

## Integrantes

- Joaquín Diaz Gonzalez
- Leonel Relmo

## Qué hizo cada uno

- **Joaquín:** `catalogo.py`, instalación del ambiente, notebook `informe.ipynb` y, en `graficos.py`, los gráficos de lanzamientos por año (simple y apilado Starlink vs. resto) y de altura media por grupo.
- **Leonel:** `satelite.py`, `analisis.py` y, en `graficos.py`, los histogramas de altitudes (órbita baja y escala logarítmica) y de inclinaciones, y el gráfico del tema libre (evolución de los tipos de órbita por año de lanzamiento).
- Ambos revisaron el código del otro y redactaron las conclusiones del informe.

## Estructura

```text
catalogo.py        lectura del catálogo, grupos y lanzamientos por año
satelite.py        clase Satelite y crear_satelites
analisis.py        conteos, extremos, ordenamiento y zonas
graficos.py        gráficos con Matplotlib (Etapa 2)
funciones_base.py  cálculos astronómicos con Skyfield (provisto)
informe.ipynb      informe: importa y usa los módulos
datos/satelites.json  catálogo de satélites (provisto)
```

## Cómo correr el proyecto

1. Crear el ambiente chico `.venv` e instalar skyfield siguiendo `instalacion.md`.
2. Activarlo desde la carpeta del proyecto:
   ```bash
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   ```
3. Abrir `informe.ipynb` (desde VS Code, eligiendo el kernel `.venv`, o con
   `python -m jupyterlab`) y ejecutar **Restart & Run All**.

Los resultados dependen del momento de ejecución (las posiciones se calculan con
la hora actual), así que algunos números, como los satélites sobre Bariloche,
cambian en cada corrida.
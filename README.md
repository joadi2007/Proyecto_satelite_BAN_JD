# Proyecto_satelite_BAN_JD

Trabajo Práctico de Programación 1 (Etapa 1): seguimiento y caracterización de satélites.
El proyecto lee un catálogo de satélites (CelesTrak), calcula su posición con Skyfield
y genera estadísticas: conteo por grupo y por tipo de órbita, lanzamientos por año,
altitudes por grupo y satélites sobre Bariloche.

## Integrantes

- Joaquín  — Diaz Gonzalez
- Leonel — Relmo

## Qué hizo cada uno

- **Joaquín:** `catalogo.py`, notebook `informe.ipynb`, instalación del ambiente.
- **Leonel:** `satelite.py` y `analisis.py`.
- Ambos revisaron el código del otro y redactaron las conclusiones del informe.

## Estructura

```text
catalogo.py        lectura del catálogo, grupos y lanzamientos por año
satelite.py        clase Satelite y crear_satelites
analisis.py        conteos, extremos, ordenamiento y zonas
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
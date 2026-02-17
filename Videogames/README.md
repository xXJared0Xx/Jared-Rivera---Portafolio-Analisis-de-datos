Dashboard de Análisis de la Industria del Videojuego

Este proyecto explora tendencias clave de la industria del videojuego mediante limpieza, transformación y modelado de datos. El dashboard permite analizar el crecimiento del sector, la calidad percibida por los usuarios y el desempeño de los distintos géneros.


Objetivos:

* Analizar la evolución de la producción de videojuegos a lo largo del tiempo
* Evaluar cambios en las valoraciones de los usuarios
* Identificar los géneros mejor valorados
* Explorar la relación entre volumen de producción y calidad percibida


Hallazgos Principales:

* La industria experimentó un crecimiento significativo a partir de los años 80
* Las valoraciones promedio se estabilizan conforme madura el sector
* Los géneros con enfoque narrativo (como Drama) reciben mejores valoraciones
* Existe una correlación positiva entre el volumen de producción y la calidad percibida



Herramientas y Tecnologías:

* Power BI — visualización y diseño del dashboard
* SQL — almacenamiento y consulta de datos
* DAX — medidas dinámicas y filtros temporales
* IMDb Datasets — fuente de datos


Preparación de Datos

Para garantizar la calidad del análisis se realizaron las siguientes tareas:

* Eliminación de registros incompletos o inconsistentes
* Filtrado de entradas con pocos votos para mejorar la confiabilidad
* Separación de géneros múltiples en tablas relacionales
* Creación de un modelo de datos optimizado para análisis


Modelo de Datos

Se implementó un modelo relacional para garantizar precisión y rendimiento:

* videojuegos — tabla principal
* videojuegos_generos — tabla puente para los géneros

Esta estructura evita duplicidades y permite un análisis escalable.



Características del Dashboard

Tarjetas KPI con métricas clave
Visualización del crecimiento de la industria
Evolución histórica de valoraciones
Gráfico de dispersión: producción vs calidad
Top géneros por valoración promedio
Filtro dinámico por periodos (últimos 5, 10 y 20 años)

Vista Previa:

[Dashboard](Dashboard.pdf)

Cómo usar el Dashboard

1. Abrir el archivo `.pbix` en Power BI Desktop
2. Utilizar el filtro temporal para explorar distintos periodos
3. Interactuar con los gráficos para analizar tendencias
4. Pasar el cursor sobre los visuales para ver detalles adicionales

[Descargar](Dashboard.pbix)

Aprendizajes Clave

Este proyecto demuestra:

* Limpieza y preparación de datos
* Modelado relacional
* Análisis exploratorio
* Visualización orientada al negocio
* Generación de insights a partir de datos

Procesamiento:
[Ver notebook](Procesamiento.ipynb)

Autor:

**Jared Dagoberto Rivera Domínguez**
Estudiante de Matemáticas Aplicadas y Computación
Interesado en análisis de datos y Business Intelligence


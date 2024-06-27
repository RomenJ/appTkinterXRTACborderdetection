RX-TAC Border-Gaussian Analyzer
Este programa interactivo de procesamiento de imágenes permite cargar imágenes, calcular histogramas, aplicar filtros de convolución y detección de bordes, y guardar los resultados procesados. Utiliza bibliotecas como Tkinter para la interfaz gráfica y Matplotlib para visualización.

Características Principales
Cargar Imagen: Permite al usuario seleccionar una imagen en formato .jpg, .jpeg o .png.
Histograma: Calcula y muestra el histograma de la imagen cargada para analizar la distribución de los valores de píxel.
Filtros Aplicados:
Convolución: Aplica un filtro de convolución para realzar ciertas características de la imagen, mostrando el resultado en una ventana separada.
Detección de Bordes: Utiliza un filtro de convolución específico para detectar bordes verticales en la imagen y muestra el resultado en una tercera ventana.
Guardar Imagen Procesada: Permite guardar la imagen procesada con detección de bordes en una carpeta de resultados local.
Interfaz Gráfica Intuitiva: Diseñada con Tkinter, proporciona botones para cada función y mensajes informativos mediante cuadros de diálogo.
Requisitos
Python 3.x
Bibliotecas:
tkinter
matplotlib
numpy
scipy
imageio
Uso
Clonar el Repositorio:



Ejecutar la Aplicación:

bash

python main.py


Interacción con la Aplicación:

Cargar Imagen: Haz clic en "Cargar Imagen" y selecciona un archivo de imagen.
Procesar Imagen: Después de cargar una imagen, haz clic en "Procesar Imagen" para ver el histograma y los efectos de los filtros aplicados.
Guardar Imagen: Una vez procesada la imagen, puedes guardarla con la detección de bordes utilizando el botón "Guardar Imagen con Detección de Bordes".
Limpiar: Para iniciar un nuevo análisis, haz clic en "Limpiar" para eliminar la imagen actual y los resultados.
Ejemplos y Recursos Adicionales
Para obtener más ejemplos de datasets de imágenes, visita:
Kaggle Datasets
Contribuciones
Contribuciones y mejoras son bienvenidas. Si encuentras algún problema o tienes alguna sugerencia, por favor abre un issue en el repositorio.

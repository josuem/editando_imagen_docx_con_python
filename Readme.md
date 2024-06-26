# Reemplazo de imagenes en documento docx usando Python
`replace_images_docx.py` es un módulo de Python que permite reemplazar imágenes en un documento DOCX con gráficos generados por Matplotlib. Este módulo es útil para automatizar la generación de reportes o documentos que incluyen gráficos actualizados.

## Características

- Reemplaza una imagen específica en un documento DOCX con un gráfico generado por Matplotlib.
- Mantiene las dimensiones del gráfico al reemplazar la imagen.
- Guarda el documento modificado con un nuevo nombre.

## Uso
Los programas pueden ser usados utilizando directamente los script de la carpeta `src` (ver `./test/prueba_reemplazo_imagen.py` como ejemplo de importación relativa) o instalando como libraria mediante

```bash
pip install -e . 
```

## Requisitos

- Python 3.x
- Bibliotecas: `python-docx`, `Pillow`, `matplotlib`

Puedes instalar las bibliotecas necesarias con pip:

```bash
pip install python-docx pillow matplotlib
```

## Limitaciones 
- Las imágenes reemplazadas son ajustadas a las dimensiones de la imagen reemplazada. Utilizar `fig, ax = plt.subplots(..., figsize=(x, y))` para reemplazar la figura utilizando las mismas proporciones.


# TODO
- [ ] Agregar librarias a un paquete único
- [ ] Crear lista de imágenes a actualizar
- [ ] Agregar V1x.0 al final del nuevo docx si no existe.
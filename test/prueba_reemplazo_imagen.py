# %% 
import io
from docx import Document

from src.view_all_image import show_all_image
from src.replace_images_docx import replace_image

# %% 
print("Muestra todas las imagenes dentro del archivo de Word.")
# Abrir el documento de Word
doc = Document('./example_1.docx')
show_all_image(doc)

# %% Creo un archivo para actualizar el gráfico actual
import matplotlib.pyplot as plt
import scienceplots
import numpy as np

plt.style.use(['science', 'notebook'])

t = np.arange(0.0, 2*np.pi, 0.01)
 
fig, ax = plt.subplots(1, figsize=(8, 7))
ax.plot(t, np.sin(t))
ax.set(xlabel='time (s)', ylabel='voltage (mV)',)

# Guardo la figura en un buffer para reemplazarlo posteriormente en el archivo docx
buf = io.BytesIO()
plt.savefig(buf, format='PNG', bbox_inches='tight')
plt.close(fig)
buf.seek(0)


# %% 
print("Reemplaza una imagen con un gráfico.")
output_file = 'documento_modificado.docx'

replace_image(doc, 1, buf, output_file=output_file)

import os

# Abrir el archivo con el programa por defecto en Windows
os.startfile(output_file)




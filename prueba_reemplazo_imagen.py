# %% Librerias
import io
from docx import Document
import os 
import sys 
import matplotlib.pyplot as plt
import scienceplots
import numpy as np

plt.style.use(['science', 'notebook'])
src_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))

if src_folder not in sys.path: 
	sys.path.append(src_folder)

from src.view_all_image import show_all_image
from src.replace_images_docx import replace_image

# %% Parámetros 
doc = Document('./test/example_1.docx')
output_file = './test/documento_modificado.docx'


# %%  Muestra todas las imagenes
print("Muestra todas las imagenes dentro del archivo de Word.")
show_all_image(doc)

# %% Creo un archivo para actualizar el gráfico actual
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
replace_image(doc, 1, buf, output_file=output_file)




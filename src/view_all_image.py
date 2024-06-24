# %% 
import io
from docx import Document
from PIL import Image
import matplotlib.pyplot as plt
import math


def show_all_image(doc):
	# Lista para almacenar las imágenes
	images = []


	# Recorrer las partes del documento en busca de imágenes
	for rel in doc.part.rels:
		if "image" in doc.part.rels[rel].target_ref:
			image_part = doc.part.rels[rel].target_part
			image_data = image_part.blob
			images.append(image_data)

	# Verificar si se encontraron imágenes
	if images:
		# Determinar el tamaño de la cuadrícula para los subplots
		num_images = len(images)
		cols = math.ceil(math.sqrt(num_images))
		rows = math.ceil(num_images / cols)

		# Crear la figura y los subplots
		fig, axs = plt.subplots(rows, cols, figsize=(15, 15))
		axs = axs.flatten()  # Aplanar la matriz de subplots para un fácil acceso

		# Mostrar cada imagen en un subplot
		for idx, image_data in enumerate(images):
			img = Image.open(io.BytesIO(image_data))
			axs[idx].imshow(img)
			axs[idx].set_title(f'Imagen {idx}')
			axs[idx].axis('off')

		# Apagar los ejes de los subplots no utilizados
		for idx in range(num_images, len(axs)):
			axs[idx].axis('off')

		# Mostrar el gráfico con subplots
		plt.tight_layout()
		plt.show()
	else:
		print("No se encontraron imágenes en el documento.")

# %% 
if __name__ == '__main__':
	# Abrir el documento de Word
	doc = Document('../example_1.docx')

	show_all_image(doc)




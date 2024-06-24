# %% 
from docx import Document
import io
from PIL import Image
import matplotlib.pyplot as plt

def crear_grafico(width=8, height=7):
    fig, ax = plt.subplots(figsize=(width, height))
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color="red")
    ax.set_title('Ejemplo de Gráfico')
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    buf = io.BytesIO()
    plt.savefig(buf, format='PNG', bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    return buf

def replace_image(doc, n_image, buf, output_file='documento_modificado.docx'):
    images = []

    # Recorrer las partes del documento en busca de imágenes
    for rel in doc.part.rels:
        if "image" in doc.part.rels[rel].target_ref:
            image_part = doc.part.rels[rel].target_part
            images.append(image_part)

    # Verificar si hay al menos una imagen
    print(f"Se encontraron {len(images)} imagenes en el documento.")
    print(f"Se reemplazara la imagen {n_image} con el gráfico.")

    if len(images) >= 1:
        image_part = images[n_image]

        # Crear el gráfico y obtener los datos de la imagen
        img = Image.open(buf)

        # Guardar la imagen modificada
        new_image_stream = io.BytesIO()
        img.save(new_image_stream, format='PNG')
        new_image_stream.seek(0)
        image_part._blob = new_image_stream.read()

        # Guardar el documento modificado
        doc.save(output_file)
        print(f"La imagen {n_image} ha sido reemplazada con el gráfico y el documento se ha guardado como '{output_file}'.")
    else:
        print("El documento no contiene suficientes imágenes.")

# %% 
if __name__ == '__main__':
    doc = Document('../example_1.docx')    
    buf = crear_grafico()
    replace_image(doc, 1, buf)
    
from setuptools import setup, find_packages

setup(
    name='replace_docx',  # Nombre del paquete que se instalará
    version='0.1',
    packages=find_packages('src'),  # Encuentra automáticamente los paquetes en la carpeta 'src'
    package_dir={'': 'src'},  # Indica que los paquetes están en la carpeta 'src'
    install_requires=[
        'docx',
        'Pillow',
        'matplotlib'
        # Agrega aquí cualquier otra dependencia necesaria
    ],
    entry_points={
        'console_scripts': [
            # Si deseas crear scripts ejecutables, puedes especificarlos aquí
        ],
    }
)

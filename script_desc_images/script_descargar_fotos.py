import requests
import csv
import os

def descargar_imagen(url, carpeta_destino):
    nombre_archivo = url.split('/')[-1].split('?')[0]  # Eliminar cualquier parte de la URL que no sea el nombre del archivo
    ruta_archivo = os.path.join(carpeta_destino, nombre_archivo)
    with open(ruta_archivo, 'wb') as archivo:
        respuesta = requests.get(url)
        archivo.write(respuesta.content)


def descargar_fotos_desde_csv(archivo_csv, carpeta_destino):
    with open(archivo_csv, newline='') as archivo:
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:
            url_imagen = fila[0]  # Suponiendo que la URL de la imagen está en la primera columna
            descargar_imagen(url_imagen, carpeta_destino)

if __name__ == "__main__":
    archivo_csv = 'enlaces.csv'  # Nombre del archivo CSV
    carpeta_destino = 'fotos'  # Carpeta donde se guardarán las fotos descargadas

    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    descargar_fotos_desde_csv(archivo_csv, carpeta_destino)

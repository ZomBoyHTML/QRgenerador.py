import qrcode
from PIL import Image

cadena = input("Insertar texto o link: ")
imagen = qrcode.make(cadena)

nombre_imagen = input("Dale un nombre a la imagen: ") + '.png'
archivo_imagen = open(nombre_imagen, 'wb')
imagen.save(archivo_imagen)
archivo_imagen.close()
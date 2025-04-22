import os

def crear_archivo_properties(nombre_png):
    # Elimina la extensión .png para obtener el nombre base del archivo
    nombre_base = os.path.splitext(nombre_png)[0]
    
    # Crea el contenido del archivo .properties
    contenido = f"""type=item
matchItems=lingering_potion
texture={nombre_base}
nbt.display.Name=ipattern:*{nombre_base.replace('_', ' ')}*
"""
    
    # Crea el archivo .properties
    nombre_properties = f"{nombre_base}.properties"
    with open(nombre_properties, 'w') as archivo:
        archivo.write(contenido)
    
    # Imprime para confirmar que se creó el archivo
    print(f"Archivo .properties creado para: {nombre_png}")

def buscar_archivos_png():
    # Obtiene los archivos en el directorio actual
    archivos_en_carpeta = os.listdir()
    
    # Imprime los archivos encontrados en la carpeta
    print("Archivos en la carpeta:", archivos_en_carpeta)
    
    # Filtra archivos con extensión .png (insensible a mayúsculas)
    archivos_png = [archivo for archivo in archivos_en_carpeta if archivo.lower().endswith('.png')]
    
    # Si no hay archivos PNG, imprime un mensaje
    if not archivos_png:
        print("No se encontraron archivos .png en la carpeta.")
        return
    
    # Para cada archivo .png encontrado, crea el archivo .properties
    for archivo_png in archivos_png:
        crear_archivo_properties(archivo_png)
    
    # Imprime al finalizar el procesamiento de todos los archivos
    print("Procesamiento finalizado.")

# Llamar a la función para procesar los archivos
buscar_archivos_png()
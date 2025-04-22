import os
import re

def extraer_nombres_de_properties(nombre_properties):
    nbt_nombre = None
    match_items = None
    
    with open(nombre_properties, 'r') as archivo:
        for linea in archivo:
            # Busca la línea que contiene "nbt.display.Name=ipattern:*"
            if "nbt.display.Name=ipattern:" in linea:
                # Usa una expresión regular para extraer el contenido entre los asteriscos
                coincidencia_nbt = re.search(r'ipattern:\*(.*?)\*', linea)
                if coincidencia_nbt:
                    nbt_nombre = coincidencia_nbt.group(1)
            
            # Busca la línea que contiene "matchItems="
            if "matchItems=" in linea:
                # Usa una expresión regular para extraer el contenido después de "matchItems="
                coincidencia_match = re.search(r'matchItems=(.*)', linea)
                if coincidencia_match:
                    match_items = coincidencia_match.group(1)
    
    return nbt_nombre, match_items

def buscar_archivos_properties():
    # Obtiene los archivos en el directorio actual
    archivos_en_carpeta = os.listdir()
    
    # Filtra solo los archivos .properties
    archivos_properties = [archivo for archivo in archivos_en_carpeta if archivo.endswith('.properties')]
    
    # Si no hay archivos properties, imprime un mensaje
    if not archivos_properties:
        print("No se encontraron archivos .properties en la carpeta.")
        return

    # Abre (o crea) el archivo nombre.txt para escribir los resultados
    with open('aanombre.txt', 'w') as archivo_salida:
        # Para cada archivo .properties encontrado
        for archivo_properties in archivos_properties:
            nbt_nombre, match_items = extraer_nombres_de_properties(archivo_properties)
            if nbt_nombre and match_items:
                # Escribe los nombres extraídos en el archivo nombre.txt
                archivo_salida.write(f"{nbt_nombre} | {match_items}\n")
                print(f" {nbt_nombre} | {match_items}")
            else:
                print(f"No se encontraron valores en el archivo {archivo_properties}")
    
    # Imprime al finalizar el procesamiento de todos los archivos
    print("Extracción finalizada. Revisa el archivo nombre.txt.")

# Llamar a la función para procesar los archivos
buscar_archivos_properties()

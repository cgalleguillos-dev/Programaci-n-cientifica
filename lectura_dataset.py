# Nombre del archivo a leer
from show_resources import get_resource_info


nombre_archivo = 'dataset.txt'  # Cambia 'ruta_del_archivo.txt' por la ruta real del archivo

# Leer el archivo y omitir las primeras 3 líneas
arch = open(nombre_archivo, 'r')
lineas = arch.readlines()[3:]

# Función save_data_1
def save_data_1(lineas):
    ids = []
    frames = []
    for linea in lineas:
        linea = linea.strip()
        id = linea.split()[0]
        frame = linea.split()[1]
        ids.append(id)
        frames.append(frame)
    return ids, frames

# Función save_data_2
def save_data_2(lineas):
    ids = [linea.split()[0] for linea in lineas]
    frames = [linea.split()[1] for linea in lineas]
    return ids, frames

# Medir recursos para la función save_data_1
print("Medición de recursos para la función save_data_1")
get_resource_info(lambda: save_data_1(lineas))

# Medir recursos para la función save_data_2
print("Medición de recursos para la función save_data_2")
get_resource_info(lambda: save_data_2(lineas))
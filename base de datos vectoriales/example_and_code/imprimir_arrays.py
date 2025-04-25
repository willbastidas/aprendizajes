import pandas as pd
import os

# Ruta específica del archivo
ruta_base = r"C:\Users\PCSISTEMAS\Documents\proyectos\excel"
nombre_archivo = "vehiculo_array.xlsx"
ruta_completa = os.path.join(ruta_base, nombre_archivo)

# Leer el archivo Excel
df = pd.read_excel(ruta_completa)

# Obtener solo la columna 'Nombre', eliminar vacíos
vehiculos = df['Nombre'].dropna().tolist()

# Ruta para guardar el archivo .txt
ruta_txt = os.path.join(ruta_base, "lista_vehiculos.txt")

# Guardar en formato de arreglo Python
with open(ruta_txt, "w", encoding="utf-8") as f:
    f.write(str(vehiculos))

print(f"Archivo guardado exitosamente en formato de array en: {ruta_txt}")

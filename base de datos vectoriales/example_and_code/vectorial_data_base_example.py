import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Paso 1: Leer tu Excel
ruta_excel = "datos_vambe.xlsx"  # Cambia esto si el archivo se llama diferente
df = pd.read_excel(ruta_excel)

# Paso 2: Definir las columnas que usarás para construir el texto base
columnas_para_vectorizar = [
    "Nombre", "Prioridad", "Valores de las variantes", "Cantidad a mano",
    "Unidad de medida", "Precio de venta", "Etiquetas de producto",
    "Descripción"
]

# Reemplazamos nulos y convertimos a texto
df = df.fillna("")
textos = df[columnas_para_vectorizar].astype(str).agg(" ".join, axis=1).tolist()

# Paso 3: Cargar el modelo de embeddings local
modelo = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = modelo.encode(textos, show_progress_bar=True)

# Paso 4: Crear la base vectorial con FAISS
dimension = len(embeddings[0])
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings).astype("float32"))

# Paso 5: Guardar los datos y el índice si quieres usarlos después
faiss.write_index(index, "base_vectorial.index")
df.to_csv("datos_originales.csv", index=False)

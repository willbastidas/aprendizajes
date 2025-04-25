import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

# Paso 1: Cargar el índice
index = faiss.read_index("base_vectorial.index")

# Paso 2: Cargar los datos originales para mostrar los resultados
df = pd.read_csv("datos_originales.csv")

# Paso 3: Cargar el modelo (debe ser el mismo que usaste antes)
modelo = SentenceTransformer("all-MiniLM-L6-v2")

# Paso 4: Hacer una búsqueda
consulta = "amortiguadores para Toyota 2020"
embedding = modelo.encode([consulta])

# Buscar los más parecidos
D, I = index.search(np.array(embedding).astype("float32"), k=3)

# Mostrar resultados
print("Resultados más parecidos:")
for i in I[0]:
    print("-" * 40)
    print(df.iloc[i])

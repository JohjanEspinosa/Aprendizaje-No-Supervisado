# Importar bibliotecas necesarias
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Paso 1: Crear un dataset de ejemplo
data = {
    'Ruta': ['A-B', 'A-C', 'B-D', 'B-E', 'C-F', 'E-F'],
    'Distancia_km': [5, 10, 4, 6, 7, 3],
    'Tiempo_estimado_min': [15, 30, 10, 20, 25, 8],
    'Pasajeros_promedio': [100, 150, 50, 80, 120, 40]
}

# Convertir a DataFrame
df_transporte = pd.DataFrame(data)

# Paso 2: Preparar los datos para K-means
X = df_transporte[['Distancia_km', 'Tiempo_estimado_min', 'Pasajeros_promedio']]

# Paso 3: Aplicar K-means
kmeans = KMeans(n_clusters=2)  # Elegimos 2 clusters
df_transporte['Cluster'] = kmeans.fit_predict(X)

# Paso 4: Mostrar resultados
print("Resultado de clustering:")
print(df_transporte)

# Paso 5: Visualizar los clusters
plt.scatter(df_transporte['Distancia_km'], df_transporte['Tiempo_estimado_min'], c=df_transporte['Cluster'], cmap='viridis')
plt.xlabel('Distancia (km)')
plt.ylabel('Tiempo Estimado (min)')
plt.title('Clusters de Rutas de Transporte')
plt.grid(True)
plt.colorbar(label='Cluster')
plt.show()

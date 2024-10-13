# Aprendizaje-No-Supervisado

Explicación del Código

1. Importación de Bibliotecas:
* Se importan pandas para la manipulación de datos, KMeans para el algoritmo de clustering, y matplotlib para la visualización.

2. Creación del Dataset:
* Se utiliza el mismo dataset ficticio de rutas que antes.

3. Preparar los Datos:
* Se seleccionan las columnas relevantes (distancia, tiempo y pasajeros) para aplicar el algoritmo K-means.

4. Aplicar K-means:
* Se crea un modelo K-means con un número específico de clusters (en este caso, 2) y se ajusta a los datos. El resultado se almacena en una nueva columna llamada 'Cluster'.

5. Mostrar Resultados:
* Se imprime el DataFrame con la nueva columna que indica a qué cluster pertenece cada ruta.

6. Visualización:
* Se utiliza un gráfico de dispersión para mostrar cómo se agrupan las rutas según las características seleccionadas.

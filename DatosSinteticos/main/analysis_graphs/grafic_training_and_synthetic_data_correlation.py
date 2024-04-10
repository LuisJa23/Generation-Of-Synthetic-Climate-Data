import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar los datos originales y los datos sintéticos
datos_originales = pd.read_csv('../../sources/weatherAUS_balanced_and_clean.csv')
datos_sinteticos = pd.read_csv('../../sources/synthetic_data_random_forest.csv')

# Calcular la matriz de correlación para los datos originales
correlaciones_originales = datos_originales.corr()

# Calcular la matriz de correlación para los datos sintéticos
correlaciones_sinteticos = datos_sinteticos.corr()

# Calcular la diferencia en las correlaciones entre los datos originales y los datos sintéticos
diferencia_correlaciones = correlaciones_sinteticos - correlaciones_originales

# Graficar las correlaciones en los datos originales sin mostrar los valores numéricos
plt.figure(figsize=(12, 6))
sns.heatmap(correlaciones_originales, cmap='coolwarm', linewidths=.5)
plt.title('Matriz de Correlación - Datos Originales')
plt.show()

# Graficar las correlaciones en los datos sintéticos con los valores numéricos
plt.figure(figsize=(12, 6))
sns.heatmap(correlaciones_sinteticos, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Matriz de Correlación - Datos Sintéticos')
plt.show()

# Graficar la diferencia en las correlaciones entre los datos originales y los datos sintéticos sin mostrar los valores numéricos
plt.figure(figsize=(12, 6))
sns.heatmap(diferencia_correlaciones, cmap='coolwarm', linewidths=.5)
plt.title('Diferencia en las Correlaciones')
plt.show()





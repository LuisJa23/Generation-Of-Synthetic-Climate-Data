import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
datos_reales = pd.read_csv('../../sources/synthetic_data_random_forest.csv')

# Contar los valores de RainToday (1 para llueve, 0 para no llueve)
lluvia_counts = datos_reales['RainToday'].value_counts()

# Crear un gráfico de barras para la comparativa
plt.bar(['No llueve', 'Llueve'], lluvia_counts, color=['blue', 'green'])
plt.title('Comparativa de días lluviosos y no lluviosos')
plt.xlabel('Condición del Tiempo')
plt.ylabel('Cantidad de Días')
plt.show()

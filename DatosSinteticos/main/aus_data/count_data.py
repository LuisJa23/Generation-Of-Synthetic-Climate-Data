import pandas as pd

# Cargar el archivo
data = pd.read_csv("../../sources/weatherAUS_balanced_and_clean.csv")

# Contar los valores únicos en la columna "RainToday"
conteo_valores = data["RainToday"].value_counts()

# Mostrar el conteo de valores
print("Conteo de valores en la columna 'RainToday':")
print(conteo_valores)
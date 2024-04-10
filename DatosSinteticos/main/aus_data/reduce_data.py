import pandas as pd

# Carga el archivo CSV
data = pd.read_csv("../../sources/weatherAUS_balanced_and_clean.csv")

# Contar el número de registros por cada valor de la columna "RainToday"
counts = data['RainToday'].value_counts()

# Mostrar el número de registros para cada categoría
print("Número de registros para cada categoría en RainToday:")
print(counts)

# Seleccionar aleatoriamente 5000 registros de cada categoría
random_samples_0 = data[data['RainToday'] == 0].sample(n=1000, random_state=42)
random_samples_1 = data[data['RainToday'] == 1].sample(n=1000, random_state=42)

# Combinar los dos conjuntos de muestras aleatorias
random_samples = pd.concat([random_samples_0, random_samples_1])

# Guardar los registros seleccionados en un nuevo archivo CSV
random_samples.to_csv("muestras_seleccionadas_2000.csv", index=False)

print("Se han guardado 5000 registros de cada categoría en el archivo 'muestras_seleccionadas.csv'.")

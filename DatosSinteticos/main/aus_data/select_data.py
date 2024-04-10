import pandas as pd

# Cargar el archivo
data = pd.read_csv("../../sources/weatherAUS.csv")

# Filtrar los datos para quedarnos solo con los "yes"
yes_data = data[data["RainToday"] == "Yes"]

# Contar cuántas filas hay con "yes"
num_yes = len(yes_data)

# Filtrar los datos para quedarnos solo con los "no"
no_data = data[data["RainToday"] == "No"]

# Tomar una muestra aleatoria de los "no" del mismo tamaño que los "yes"
no_data_sample = no_data.sample(n=num_yes, random_state=42)

# Concatenar los datos "yes" y los "no" seleccionados aleatoriamente
balanced_data = pd.concat([yes_data, no_data_sample])

# Guardar los datos balanceados en otro archivo
balanced_data.to_csv("../../sources/weatherAUS_balanced.csv", index=False)

print("Se han guardado los datos balanceados en 'datos_balanceados.csv'")

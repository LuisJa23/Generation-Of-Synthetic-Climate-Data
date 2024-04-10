import pandas as pd

# Cargar el archivo
data = pd.read_csv("../../sources/weatherAUS_balanced.csv")

# Eliminar las columnas 'Date' y 'Location'
data = data.drop(columns=['Date', 'Location', 'WindGustDir', 'WindDir9am','WindDir3pm', 'RainTomorrow'])

# Mapear los valores de 'RainToday' y 'RainTomorrow' a 1 si es 'Yes' y 0 si es 'No'
data['RainToday'] = data['RainToday'].map({'Yes': 1, 'No': 0})

# Guardar los cambios en un nuevo archivo CSV
data.to_csv("../../sources/weatherAUS_balanced_and_clean.csv", index=False)

print("Se han eliminado las columnas 'Date' y 'Location', y se han mapeado los valores de 'RainToday'")

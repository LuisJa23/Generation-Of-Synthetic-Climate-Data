import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

# Cargar datos reales desde el archivo CSV
datos_reales = pd.read_csv('../../sources/weatherAUS_balanced_and_clean.csv')

# Dividir los datos en variables independientes (X) y variable objetivo (y)
X = datos_reales[['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
                  'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am',
                  'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am',
                  'Cloud3pm', 'Temp9am', 'Temp3pm']]
y = datos_reales['RainToday']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definir el número de árboles (estimadores) y la profundidad máxima
n_estimators = 100
max_depth = 10

# Crear el modelo RandomForestClassifier
rf_model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
rf_model.fit(X_train, y_train)

# Generar datos sintéticos utilizando el modelo entrenado
datos_sinteticos = []

num_datos_sinteticos = 24924
for _ in range(num_datos_sinteticos):
    # Generar valores aleatorios para las variables independientes
    datos_generados = {}
    for col in X.columns:
        # Generar un valor aleatorio basado en la distribución aprendida por el modelo
        if col == 'Rainfall':
            # La variable Rainfall está condicionada por la variable objetivo
            prediccion = np.random.choice(['Yes', 'No'], p=rf_model.predict_proba(X.sample())[0])
            if prediccion == 'Yes':
                datos_generados[col] = np.random.uniform(0, X[col].max())
            else:
                datos_generados[col] = 0
        else:
            datos_generados[col] = np.random.uniform(X[col].min(), X[col].max())

    # Agregar los datos generados a la lista de datos sintéticos
    datos_sinteticos.append(datos_generados)

    # Generar la predicción de RainToday y agregarla al diccionario de datos generados
    X_synthetic = pd.DataFrame([datos_generados])
    prediccion_rain_today = rf_model.predict(X_synthetic)[0]
    datos_generados['RainToday'] = prediccion_rain_today

# Convertir la lista de datos sintéticos en un DataFrame
datos_sinteticos_df = pd.DataFrame(datos_sinteticos)

# Guardar los datos sintéticos en un archivo CSV
datos_sinteticos_df.to_csv('../../sources/synthetic_data_random_forest.csv', index=False)

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Cargar los datos originales y los datos sintéticos
datos_originales = pd.read_csv('../../sources/weatherAUS_balanced_and_clean.csv')
datos_sinteticos = pd.read_csv('../../sources/synthetic_data_random_forest.csv')

# Dividir los datos en variables independientes (X) y variable objetivo (y)
X_originales = datos_originales[['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
                                 'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am',
                                 'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am',
                                 'Cloud3pm', 'Temp9am', 'Temp3pm']]
X_sinteticos = datos_sinteticos[['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine',
                                  'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am',
                                  'Humidity3pm', 'Pressure9am', 'Pressure3pm', 'Cloud9am',
                                  'Cloud3pm', 'Temp9am', 'Temp3pm']]

# Normalizar los datos para que tengan media 0 y desviación estándar 1
scaler = StandardScaler()
X_originales_scaled = scaler.fit_transform(X_originales)
X_sinteticos_scaled = scaler.transform(X_sinteticos)

# Aplicar PCA a los datos originales y a los datos sintéticos
pca = PCA(n_components=2)
X_originales_pca = pca.fit_transform(X_originales_scaled)
X_sinteticos_pca = pca.transform(X_sinteticos_scaled)

# Crear dos gráficos independientes con la misma escala
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Graficar los resultados del PCA para datos originales
axs[0].scatter(X_originales_pca[:, 0], X_originales_pca[:, 1], color='blue', alpha=0.7, s=10)
axs[0].set_title('Datos Originales')
axs[0].set_xlabel('Componente Principal 1')
axs[0].set_ylabel('Componente Principal 2')
axs[0].grid(True)

# Graficar los resultados del PCA para datos sintéticos
axs[1].scatter(X_sinteticos_pca[:, 0], X_sinteticos_pca[:, 1], color='red', alpha=0.7, s=10)
axs[1].set_title('Datos Sintéticos')
axs[1].set_xlabel('Componente Principal 1')
axs[1].set_ylabel('Componente Principal 2')
axs[1].grid(True)

plt.tight_layout()
plt.show()

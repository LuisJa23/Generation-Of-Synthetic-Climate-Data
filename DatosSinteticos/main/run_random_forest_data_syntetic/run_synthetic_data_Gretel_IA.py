import joblib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Cargar el conjunto de datos
data = pd.read_csv('../../sources/synthetic_data_Gretel_IA.csv')

# Dividir el conjunto de datos en características (X) y etiquetas (y)
X = data.drop(['RainToday'], axis=1)
y = data['RainToday']

# Convertir variables categóricas a variables dummy
categorical_cols = []
X = pd.get_dummies(X, columns=categorical_cols)

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar solo las columnas numéricas usando StandardScaler
numeric_cols = ['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine', 'WindGustSpeed',
                'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm', 'Pressure9am',
                'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am', 'Temp3pm']
scaler = StandardScaler()
X_train[numeric_cols] = scaler.fit_transform(X_train[numeric_cols])
X_test[numeric_cols] = scaler.transform(X_test[numeric_cols])

# Random Forest
# Crear el modelo de Random Forest
rf_classifier = RandomForestClassifier(n_estimators=200, max_depth=20)
rf_classifier.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred_rf = rf_classifier.predict(X_test)

# Evaluar el rendimiento del modelo de Random Forest
accuracy_rf = accuracy_score(y_test, y_pred_rf)
conf_matrix_rf = confusion_matrix(y_test, y_pred_rf)
classification_rep_rf = classification_report(y_test, y_pred_rf)

# Guardar el modelo entrenado en un archivo
# joblib.dump(rf_classifier, 'random_forest_model.joblib')

# Resultados de Random Forest
print("\nResultados de Random Forest:")
print(f'Accuracy (Random Forest): {accuracy_rf}')
print(f'Confusion Matrix (Random Forest):\n{conf_matrix_rf}')
print(f'Classification Report (Random Forest):\n{classification_rep_rf}')




import pandas as pd
import numpy as np

diccionario = {
    'name': ["kevin", "George", "Jane", "Mel", "Thomas", "Erica", "Lisa"],
    'age': [20, 27, 35, 55, 18, 21, 35],
    'salary': [30000, 45000, 55000, 78000, 28000, 32000, 70000],
    'gender': ['m', 'm', 'f', 'f', 'm', 'f', 'f']
}

data = pd.DataFrame(diccionario)
data.head()

mayor_salario = data["salary"].max()
menor_salario = data["salary"].min()

print("Diferencia:", (mayor_salario-menor_salario))

# Actividad avanzada
print("Media:", data["salary"].mean())
print("Mediana:", data["salary"].median())
print("Desviacion estandar:", data["salary"].std())
print("Sumatoria:", data["salary"].sum())

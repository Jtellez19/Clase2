import pandas as pd
import matplotlib.pyplot as plt
hoja = pd.read_csv(
    'C:\\Users\\JTELLEZ\\Downloads\\clean_students_complete.csv')
hoja_clean = hoja.drop(["Unnamed: 0"], axis=1)

# Mostrar cuantos estudiantes hay por grado
hoja_clean[["grade", "student_name"]].groupby(
    "grade", as_index=False).count().rename(columns={"student_name": "conteo"})

# Mostrar info graficamente
hoja_clean[["grade", "student_name"]].groupby(
    "grade", as_index=False).count().rename(columns={"student_name": "conteo"}).plot(kind="bar")

import pandas as pd
import matplotlib.pyplot as plt
# obtener mejor promedio por escuela y grado
hoja = pd.read_csv(
    'C:\\Users\\JTELLEZ\\Downloads\\clean_students_complete.csv')
best_reading = hoja[hoja["reading_score"] == hoja["reading_score"].max()]
grafica = best_reading[["school_name", "student_name"]].groupby(
    "school_name", as_index=False).agg("count")
grafica.plot(kind="bar")

# obtener genero que predomina
best_gender_reading = best_reading[["school_name", "student_name", "gender"]].groupby(
    ["school_name", "gender"], as_index=False).agg("count")
grafica = best_gender_reading.groupby("school_name", as_index=False).max()
grafica[["school_name", "student_name"]].plot(kind="bar")

##########################################

# obtener peor promedio por escuela y grado
worst_reading = hoja[hoja["reading_score"] == hoja["reading_score"].min()]
grafica = worst_reading[["school_name", "student_name"]].groupby(
    "school_name", as_index=False).agg("count")
grafica.plot(kind="bar")

# obtener genero que predomina
worst_gender_reading = worst_reading[["school_name", "student_name", "gender"]].groupby(
    ["school_name", "gender"], as_index=False).agg("count")
grafica = worst_gender_reading.groupby("school_name", as_index=False).max()
grafica[["school_name", "student_name"]].plot(kind="bar")

# Coeficiente de correlacion y grafica de correlacion
worst_reading[["student_name", "reading_score",
               "math_score"]].corr(method="pearson")
plt.scatter(worst_reading["reading_score"], worst_reading["math_score"])
plt.show()

import pandas as pd

# obtener mejor promedio por escuela y grado
hoja = pd.read_csv(
    'C:\\Users\\JTELLEZ\\Downloads\\clean_students_complete.csv')
escuelaGrado = hoja.groupby(["school_name", "grade"], as_index=False).mean(
).sort_values(["school_name", "grade"])
mejores = escuelaGrado[escuelaGrado.groupby(["school_name"])[
    "reading_score"].transform(max) == escuelaGrado["reading_score"]]
mejores["reading_score"].sort_values().plot(kind="bar")

# obtener genero que predomina del filtro anterior
mejores_v2 = mejores.drop(["Student ID", "Unnamed: 0"], axis=1)
hoja_2 = hoja[["school_name", "grade", "gender"]].groupby(
    ["school_name", "grade", "gender"], as_index=False).value_counts("gender")
mergeV = pd.merge(mejores_v2, hoja_2, on=["school_name", "grade"])
mergeV[mergeV["count"] == mergeV["count"].max()]

import pandas as pd
hoja = pd.read_csv('C:\\Users\\JTELLEZ\\Downloads\\athlete_events.csv')
hoja = hoja[hoja["Medal"].notna()]

# Agrupar medallas por anio
datos = hoja[["Year", "Medal"]].groupby(["Year", "Medal"]).value_counts()[:3]
# Lista de nombres de medallas
nombres = datos.unique()
# Grafica de pay
hoja[["Year", "Medal"]].groupby(["Year", "Medal"]).value_counts(
)[:3].plot.pie(figsize=(11, 6), labels=nombres, autopct="%0.1f%%")

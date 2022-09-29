import pandas as pd
# Actividad
hoja = pd.read_csv('C:\\Users\\JTELLEZ\\Downloads\\athlete_events.csv')
hoja = hoja[hoja["Medal"].notna()]
hoja_v2 = hoja[["NOC", "Medal"]].groupby(
    "NOC", as_index=False).value_counts("Medal")
hoja_v3 = hoja_v2[["NOC", "count"]].groupby("NOC").sum()
hoja_v3.sort_values(by="count", ascending=False)[:10].plot(kind="bar")

# Activiad avanzada
hoja_v4 = hoja_v3[["NOC", "count"]].groupby(
    "NOC").sum().sort_values(by="count")
hoja_v4.plot(kind="bar")

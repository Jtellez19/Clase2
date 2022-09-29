import pandas as pd
import numpy as np

# Actividad 1
hoja = pd.read_csv('C:\\Users\\JTELLEZ\\Downloads\\athlete_events.csv')
# retiro na's de personas sin medallas
medal_notna = hoja[hoja["Medal"].notna()]
# obtengo solo las personas que tienen medallas
just_medals = medal_notna[medal_notna["Medal"].isin(
    ["Gold", "Silver", "Bronze"])]
veteran_age = just_medals["Age"].max()  # obtengo edad del competidor mas viejo
# Listo al atleta mas viejo con medalla
just_medals[just_medals["Age"] == veteran_age]
rookie_age = just_medals["Age"].min()  # obtengo edad del competidor mas joven
# Listo al atleta mas mas joven con medalla
just_medals[just_medals["Age"] == veteran_age]
# Agrupar por nombre y contar cada registro de cada columna
grp = just_medals.groupby(["Name"]).count()
# Obtengo los datos de quien tenga la mayor cantidad de medallas
name_athlete = grp[grp["Medal"] == grp["Medal"].max()]
info = hoja[hoja["Name"] == name_athlete]
# importar un csv del atleta mas ganador
info.to_csv('C:\\Users\\JTELLEZ\\Downloads\\athlete_winner.csv')


# Actividad Avanzada
noc1 = just_medals[just_medals["NOC"].isin(["MEX", "COL", "ARG"])]
veteran_age = noc1["Age"].max()
noc1[just_medals["Age"] == veteran_age]

noc2 = just_medals[just_medals["NOC"].isin(["USA", "CAN"])]
rookie_age = noc2["Age"].min()
noc2[just_medals["Age"] == rookie_age]

noc3 = just_medals[just_medals["NOC"].isin(["USA", "CHN", "RUS"])]
grp = noc3.groupby(["Name"]).count()
# Obtengo los datos de quien tenga la mayor cantidad de medallas
name_athlete = grp[grp["Medal"] == grp["Medal"].max()]
info = hoja[hoja["Name"] == name_athlete]
# importar un csv del atleta mas ganador
info.to_csv('C:\\Users\\JTELLEZ\\Downloads\\athlete_winner_v2.csv')

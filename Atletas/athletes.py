import pandas as pd
import numpy as np

##Actividad 1
hoja = pd.read_csv('C:\\Users\\JTELLEZ\\Downloads\\athlete_events.csv')
medal_notna = hoja[hoja["Medal"].notna()]##retiro na's de personas sin medallas
just_medals = medal_na[medal_na["Medal"].isin(["Gold","Silver","Bronze"])]##obtengo solo las personas que tienen medallas
veteran_age = just_medals["Age"].max()##obtengo edad del competidor mas viejo
just_medals[juest_medals["Age"]==veteran_age]##Listo al atleta mas viejo con medalla
rookie_age = just_medals["Age"].min()##obtengo edad del competidor mas joven
just_medals[juest_medals["Age"]==veteran_age]##Listo al atleta mas mas joven con medalla
grp = just_medals.groupby(["Name"]).count() ##Agrupar por nombre y contar cada registro de cada columna
name_athlete = grp[grp["Medal"] == grp["Medal"].max()] ## Obtengo los datos de quien tenga la mayor cantidad de medallas
info = hoja[hoja["Name"] == name_athlete]
info.to_csv('C:\\Users\\JTELLEZ\\Downloads\\athlete_winner.csv')## importar un csv del atleta mas ganador


##Actividad Avanzada
noc1  = just_medals[juest_medals["NOC"].isin(["MEX","COL","ARG"])]
veteran_age = noc1["Age"].max()
noc1[juest_medals["Age"]==veteran_age]

noc2  = just_medals[juest_medals["NOC"].isin(["USA","CAN"])]
rookie_age = noc2["Age"].min()
noc2[juest_medals["Age"]==rookie_age]

noc3 = just_medals[juest_medals["NOC"].isin(["USA","CHN","RUS"])]
grp = noc3.groupby(["Name"]).count()
name_athlete = grp[grp["Medal"] == grp["Medal"].max()] ## Obtengo los datos de quien tenga la mayor cantidad de medallas
info = hoja[hoja["Name"] == name_athlete]
info.to_csv('C:\\Users\\JTELLEZ\\Downloads\\athlete_winner_v2.csv')## importar un csv del atleta mas ganador
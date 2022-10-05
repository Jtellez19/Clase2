import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
hoja = pd.read_csv('C:\\Users\\JTELLEZ\\Documents\\DataSetBarrasPerdidas.csv')

hoja_torque = hoja[hoja["ClaVariable"] == 2]

agrupado_torque = hoja_torque.groupby(
    ["NomPuntoMedicion", "JobId"], as_index=False).max()

agrupado_torque[["NomPuntoMedicion", "JobId"]].groupby(
    ["NomPuntoMedicion"], as_index=False).agg("count")

conteo_torque = agrupado_torque[["NomPuntoMedicion", "JobId"]].groupby(
    ["NomPuntoMedicion"], as_index=False).agg("count").rename(columns={"JobId": "conteo"}).sort_values(by="conteo")

conteo = conteo_torque["conteo"].to_list()
pmed = conteo_torque["NomPuntoMedicion"].to_list()
plt.figure(figsize=(12, 12))
plt.pie(conteo, labels=pmed, autopct="%0.1f %%")
plt.axis("equal")
plt.show()

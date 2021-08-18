import numpy as np   # rapido
import pandas
import pandas as pd  # potencia
import matplotlib.pyplot as plt
import matplotlib



datos=pd.read_csv("mlb_players.csv",quotechar='"',skipinitialspace=True,)

print(datos) # pandas (dataframe)

agrupar=datos.groupby(by="Position") # dataframegroup

conteo_agrupacion: pandas.Series=agrupar["Name"].count() # series

conteo_agrupacion= conteo_agrupacion.sort_values()


conteo_agrupacion=conteo_agrupacion[0:5]  # rango de valores

indices=conteo_agrupacion.index.values  # ndarray
valores=conteo_agrupacion.values # ndarray

print(indices)
print(valores)

fig, ax = plt.subplots()
# ax: matplotlib.axes._subplots.AxesSubplot
# fig matplotlib.figure.Figure

# ax2=matplotlib.axes._subplots.AxesSubplot()

indicesnumericos=np.arange(len(indices)) # 0,1,2,3.

ax.set_yticks(indicesnumericos)
ax.set_yticklabels(indices)

ax.barh(indicesnumericos,valores)

plt.show()
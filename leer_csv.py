import numpy as np
import pandas as pd


datos=pd.read_csv("mlb_players.csv",quotechar='"',skipinitialspace=True,)

print(datos)

# suma por el eje (axis=0 columnas, axis=1 filas)
print(datos.sum(axis=0))

# columnas
print(datos['Age'].mean())
print(datos['Age'].min())
print(datos['Age'].max())

# obtener fila
print(datos.iloc[1])

# filtro
#           datos['Team']=='BAL'  (filtro de datos), series
#     datos[                    ] (si es true, entonces se muestra la fila)
#                                ['Age'] Obtengo la fila de la edad
#                                       .Mean() obtengo el promedio
print(datos[datos['Team']=='BAL']['Age'].mean())

# series son las filas de un dataframe (indice y los valores)
columnas=datos['Team']
series=datos['Team']=='BAL'
print(series)

# buscar todos los jugadores que son catcher y ademas del equipo WAS
filtros1=datos['Position']=="Catcher" # series
filtros2=datos['Team']=='WAS'  # series
print(datos[filtros1][filtros2])


# todos los jugadores que son catcher o son Shortstop.
filtros1=datos['Position']=="Catcher" # series
filtros2=datos['Position']=="Shortstop" # series
df_filtro1=datos[filtros1]   # dataframe de todos los catcher
df_filtro2=datos[filtros2]   # dataframe de todos los shortstop
# control+q (para ver la ayuda)
print(pd.concat([df_filtro1,df_filtro2]))

print(pd.concat([
    datos[datos['Position']=="Catcher"],
    datos[datos['Position']=="Shortstop"],
    ]))
print("agrupamiento:")
agrupamiento=datos.groupby(by=["Team","Name"])
agrupamiento_promedio_edad=agrupamiento.mean()
print(agrupamiento_promedio_edad)
# iloc (entero), loc(stringo)
print("fila WAS de la agrupacion:")
print(agrupamiento_promedio_edad.loc["WAS"])





import numpy as np   # rapido
import pandas
import pandas as pd  # potencia
import matplotlib.pyplot as plt
import matplotlib

datos=pd.read_csv("percent_bachelors_degrees_women_usa.csv")

datos=datos.sort_values(by="Architecture",ascending=False)
datos=datos[:10]
print(datos)

print(datos["Year"])

print(datos["Architecture"])

fig, ax = plt.subplots()

indicefalso=np.arange(len(datos["Year"])) # 0,1,2,3....

ax.bar(indicefalso,datos["Architecture"])

ax.set_xticks(indicefalso)
ax.set_xticklabels(datos["Year"])

plt.show()
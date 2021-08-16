import numpy as np
import pandas as pd

# numpy ndarray (multiples dimesiones)
# pandas dataframes (dos dimensiones)

df=pd.DataFrame({
    'nombre':['cocacola','fanta','sprite'],
    'precio':[10,20,30],
    'categoria':['cat1','cat2','cat3']
})

print(df)
print("pandas:")
print(df['nombre'])  # pandas estoy obteniendo la columna
print("ndarray:")
print(df.values[:,0])  # ndarray

df=pd.DataFrame(data=[[1,2],[3,4]],columns=["col1","col2"],dtype=int,index=[0,1])
print("dataframe2")
print(df)
print("transponer")
print(df.transpose())
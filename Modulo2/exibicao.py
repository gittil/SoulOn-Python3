import numpy as np
import pandas as pd

df = pd.DataFrame({'Aluno':["José", "Carlos", "Ana", "Julia", "Debora"],
                   'Faltas':[3,4,2,4,3],
                   'Prova': [2,7,8,5.5,9.2],
                   'Seminario':[8.5,5,8.2,6,9.5]})

print(df)
print("-------------------------------------")
print(df.dtypes)
print("-------------------------------------")
print(df.columns)
print("-------------------------------------")
print(df['Aluno'])
print("-------------------------------------")
print(df.describe())
print("-------------------------------------")
print(df.sort_values(by="Seminario"))
print("-------------------------------------")
print(df.loc[3])
print("-------------------------------------")
print(df[df["Seminario"]>8.0])
print("-------------------------------------")
print(df[(df["Seminario"]>8.0) & (df["Prova"]>3)])

import numpy as np
import pandas as pd

notas = pd.Series([10,5,7.5,9,10])
print(notas)


notas2 = pd.Series([10,5,7.5,9,10],index=['José', 'Carlos','André','Pedro', 'Maria'])#Atribuir Indices
print(notas2)

print(notas.describe())
print(notas.mean())
print(notas**2)
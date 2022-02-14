
from cmath import nan
import numpy as np
import pandas as pd


df_csv = pd.read_csv("/home/douglas/soulcode/SoulOn-Python3/Modulo2/dados.csv")

print(df_csv['bairro'].unique())
print("------------------------------------------------------------------")
print(df_csv['bairro'].value_counts())
print("------------------------------------------------------------------")
print(df_csv.groupby("bairro").mean())
print("------------------------------------------------------------------")


df2 = df_csv.head()
print(df2)
print("------------------------------------------------------------------")

df3 = df2.replace({"pm2":{12031.25:nan}})
print(df3)
print("------------------------------------------------------------------")

df4 = df3.dropna()
print(df4)
print("------------------------------------------------------------------")

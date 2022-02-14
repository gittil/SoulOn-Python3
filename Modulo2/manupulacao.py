
from cmath import nan
import numpy as np
import pandas as pd

#carregando o csv
df_csv = pd.read_csv("/home/douglas/soulcode/SoulOn-Python3/Modulo2/dados.csv")

# pritando na tela os valores unicos da coluna "bairro"
print(df_csv['bairro'].unique())
print("------------------------------------------------------------------")

# printando na tela a contagem de quantas vezes cada valor aparece na coluna "bairro"
print(df_csv['bairro'].value_counts())
print("------------------------------------------------------------------")

# pritando na tela o valor medio de cada barrio obtido atraves do groupby
print(df_csv.groupby("bairro").mean())
print("------------------------------------------------------------------")

# criando um novo DF a partir de um filtro passada no DF anterior
df2 = df_csv.head()
print(df2)
print("------------------------------------------------------------------")

# criando um novo DF a partir de uma alteracao feita no DF anterior
df3 = df2.replace({"pm2":{12031.25:nan}}) #funcao replace troca o valor estipulado na coluna por outro
# replace.({"nome_da_coluna":{valor a ser substituido:novovalor}})
print(df3)
print("------------------------------------------------------------------")

# criando um novo DF a partir de uma alteracao feita no DF anteriro
df4 = df3.dropna() #funcao dropna apagada do DF todas as celulas que contem informaçao vazia
print(df4)
print("------------------------------------------------------------------")

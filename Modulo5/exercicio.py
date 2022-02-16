import pandas as pd
import seaborn as sns
import plotly.express as px 
import matplotlib.pyplot as plt

market = pd.read_csv('D:\Python\SoulOn-Python3\Modulo5\supermarket_sales.csv')

df = pd.DataFrame(market)
df.head()

#seaborn
sns.countplot(df['Gender'])

#plotly
fig = px.histogram(df,x='Total')
fig.show()

#matplotlib
fig, ax = plt.subplots()
data = df['Gender'].value_counts()
genero = data.index
frequency = data.values

ax.bar(genero,frequency)
ax.set_title('Generos por compra')
ax.set_xlabel('Genero')
ax.set_ylabel('Frequencia')


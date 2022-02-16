import pandas as pd
import seaborn as sns
import plotly.express as px 


market = pd.read_csv('D:\Python\SoulOn-Python3\Modulo5\supermarket_sales.csv')

df = pd.DataFrame(market)
#df.head()
#seaborn
#sns.countplot(df['Gender'])

#plotly
#fig = px.histogram(df,x='Total')
#fig.show()

#matplotlib


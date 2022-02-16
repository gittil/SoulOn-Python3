import pandas as pd
import matplotlib as mpl

iris = pd.read_csv("iris.csv", names=['sepal_length','sepal_width','petal_length','petal_width','class'])

wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)

iris.plot.scatter(x='sepal_length',y='sepal_width', title='Iris Dataset')

wine_reviews['volatile_acidity'].plot.hist()

wine_reviews['style'].value_counts().sort_index().plot.bar()


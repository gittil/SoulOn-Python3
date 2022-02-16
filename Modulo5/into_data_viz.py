import pandas as pd

iris = pd.read_csv("iris.csv", names=['sepal_length','sepal_width','petal_length','petal_width','class'])

wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)

iris.head()


wine_reviews.head()

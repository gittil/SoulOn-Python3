import pandas as pd
import seaborn as sns 

iris = pd.read_csv("iris.csv", names=['sepal_length','sepal_width','petal_length','petal_width','class'])

wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)

sns.scatterplot(x='sepal_length',y='sepal_width', data=iris)

sns.displot(wine_reviews['volatile_acidity'],bins=10,kde=True)

sns.countplot(wine_reviews['volatile_acidity'])
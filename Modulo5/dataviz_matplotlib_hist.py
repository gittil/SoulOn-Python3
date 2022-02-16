import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("iris.csv", names=['sepal_length','sepal_width','petal_length','petal_width','class'])

wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)

fig, ax = plt.subplots()

ax.hist(wine_reviews['style'])

ax.set_title('Wine Review Scores')
ax.set_xlabel('Style')
ax.set_ylabel('Frequency')


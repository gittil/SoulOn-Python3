import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("iris.csv", names=['sepal_length','sepal_width','petal_length','petal_width','class'])

wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)

columns = iris.columns.drop(['class'])
x_data = range(0, iris.shape[0])
fig,ax = plt.subplots()

for column in columns:
    ax.plot(x_data, iris[column],label=column)
    
ax.set_title('Iris Dataset')
ax.legend()


#https://meet.google.com/qse-inxa-ejo
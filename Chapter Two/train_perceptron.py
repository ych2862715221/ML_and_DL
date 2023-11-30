import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from perceptron import Perception

s = 'https://archive.ics.uci.edu/ml/' \
    'machine-learning-databases/iris/iris.data'
print("From URL",s)
df = pd.read_csv(
    s,
    header=None,
    encoding='utf-8'
)
df.tail()

# Select setosa and versicolor
y = df.iloc[0:100,4].values
y = np.where(y == 'Iris-setosa', 0, 1)

# Extract sepal length and petal length
X = df.iloc[0:100, [0,2]].values

# Plot data
plt.scatter(
    X[50:100, 0], X[:50, 1],
    color='red', marker='o', label='Setosa'
)
plt.scatter(
    X[50:100, 0], X[50:100, 1],
    color='blue', marker='s', label='Versicolor'
)
plt.xlabel('Sepal length [cm]')
plt.ylabel('Petal length [cm]')
plt.legend(loc='upper left')
plt.show()

# Training
ppn = Perception(eta=0.1, n_iter=10)
ppn.fit(X, y)
plt.plot(
    range(1, len(ppn.errors_) +  1),
    ppn.errors_,
    marker='o'
)
plt.xlabel('Epoches')
plt.ylabel('Number of updates')
plt.show()

"""显示决策边界"""
from Plot_decision_regions import *

plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('Sepal length [cm]')
plt.ylabel('Petal length [cm]')
plt.legend(loc='upper left')
plt.show()
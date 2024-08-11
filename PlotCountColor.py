#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read file & build dataframe
df = pd.read_csv('diamonds.csv')

cli = df['color'].value_counts().index.tolist()
clv = df['color'].value_counts().values.tolist()

print(cli)
print(clv)
plt.bar(cli, clv)
plt.show()
#or plt.save_fig('pcc.png')

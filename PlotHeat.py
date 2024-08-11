#import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read file & build dataframe
df = pd.read_csv('diamonds.csv')

#drop the index column
df = df.drop('Unnamed: 0', axis=1)
df = df.select_dtypes(exclude=[object])

f, ax = plt.subplots(figsize=(10, 8))
corr = df.corr()
print(corr)
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=bool), cmap=sns.diverging_palette(220, 10, as_cmap=True), 
            square=True, ax=ax)
plt.show()

#import library
import numpy as  np
import pandas as pd
import matplotlib.pyplot as plt

#read file and build dataframe
df = pd.read_csv('diamonds.csv')

#count each textual of clarity
cli = df['clarity'].value_counts().index.tolist()
clv = df['clarity'].value_counts().values.tolist()
print(cli)
print(clv)

plt.bar(cli, clv)
plt.show()
#plt.savefig('pcc.png')

#import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read diamonds csv file and build dataframe
df = pd.read_csv('diamonds.csv')

carat = df.carat
clarity = df.clarity
plt.scatter(clarity, carat)
plt.show()
#or plt.save_fig('cvc.png')
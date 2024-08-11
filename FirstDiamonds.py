#import panda & numpy lib
import numpy as np
import pandas as pd

#read the diamonds csv file
#build data frame for the data
df = pd.read_csv('diamonds.csv')
print(df.head(10))
print()

#calculate total value of diamonds
sum = df.price.sum()
print("Total $ value of diamonds: ${:0,.2f}".format(sum))

#calculate mean price of diamonds
mean = df.price.mean()
print("Mean $ value of diamonds: ${:0,.2f}".format(mean))

#summarize the data
descrip = df.carat.describe()
print()
print(descrip)

descrip = df.describe(include='object')
print()
print(descrip)

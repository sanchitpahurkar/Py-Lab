import pandas as pd

df = pd.read_csv("fifa_data.csv")
print(df)
mean = df['Overall'].mean()
print('Mean = ',mean)
median = df['Overall'].median()
print('Median = ', median)
sd = df['Overall'].std()
print('Standard Deviation = ', sd)
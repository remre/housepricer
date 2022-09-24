import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df =pd.read_csv('C:/Users/emreb/Documents/projects/houserentpre/dts/House_Rent_Dataset.csv')
df2=df.copy()
df2 = df2.join(df['Floor'].str.split(' out of ', 1, expand=True).rename(columns={0:'floor level', 1:'total floor'}))
df2['floor level'] = df2.apply(lambda x: 0 if x['floor level'] =='Ground' \
                               else ( -2 if x['floor level'] =='Lower Basement' else -1 if x['floor level'] =='Upper Basement' else (x['floor level']) ) , axis=1)
print("Status: Changed 'Ground'=0, 'Lower Basement'=-1, Rest = total floor")
df2.drop('Floor',axis=1,inplace=True)
# print(df['City'].unique())
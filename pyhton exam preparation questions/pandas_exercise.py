import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


exam_data={'name':['Anastasia','Dima','Katherine','James','Emily','Michael','Matthew','Laura','Kevin','Jonas'], 
          'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
          'attempts':[1,3,2,3,2,3,1,1,2,1],
          'quality':['yes','no','yes','no','no','yes','yes','no','no','yes']}
lables=['a','b','c','d','e','f','g','h','i','j']

df=pd.DataFrame(exam_data)
print(df)

print(df.iloc[0:3])

print("\n",df[['name','score']])
print("Number of attempts in the examination is greater than 2: ")
print(df[df['attempts']>2])

print(df[df['score'].isnull()])

print(df[df['score'].between(10,15)])


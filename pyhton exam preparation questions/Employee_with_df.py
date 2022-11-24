import pandas as pd
dict={'empid':[12115832,12116293,12113167,12114341,12115643,12113454,12456576,12345434],
       'empname':['kallam','Anantha','Kotireddy','Mallikarjun','Naagu','Madhu','Kiran','vinukonda'],
       'Salary':[60000,50000,40000,44000,55000,60000,66000,45000]}

df=pd.DataFrame(dict)
print(df)

print(df.Salary.max())

print(df[df.Salary==df.Salary.max()])

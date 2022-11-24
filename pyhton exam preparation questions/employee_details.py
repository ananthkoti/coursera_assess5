import pandas as pd

df = pd.read_excel('C:/Users/kalla/Desktop/EmployeeData.xlsx')

print(df)


#Display Particular Department
import pandas as pd

df = pd.read_excel('C:/Users/kalla/Desktop/EmployeeData.xlsx')

print(df[df['Department']=='HR'])


#Display Employee Whose Salary Between 40k t0 60k
import pandas as pd


df = pd.read_excel('C:/Users/kalla/Desktop/EmployeeData.xlsx')

print(df[df['Salary']])


#Display the employees with range of hiring date
print((df[df['Hiring Date']>'2021-06-21']))
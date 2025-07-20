import pandas as pd
import numpy as np

data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82],
    'Gender':['Male','Male','Female']

}
df = pd.DataFrame(data)

#Min-Max scaling
#FORMULA = Normalized value = x-min/max-min
print("Min-Max scaling for maths scores")
df['Math_Normalized'] = (df['Math']-df['Math'].min()) / (df['Math'].max()-df['Math'].min())
#updated daframe
print(df[['Name' , 'Math','Math_Normalized']])

print("Add a Gender Column")
#df['Gender'] = ['Male','Male','Female']
#One-Hot encode
df_encoded = pd.get_dummies(df,columns=['Gender'],dtype=int)
print(df_encoded)

print("group students by gender Average Marks ")
avg_marks_by_group = df.groupby('Gender')[['Math','Science','English']].mean()
print(avg_marks_by_group)
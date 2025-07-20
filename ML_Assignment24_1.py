import pandas as pd
import numpy as np

data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]

}
df = pd.DataFrame(data)

#Min-Max scaling
#FORMULA = Normalized value = x-min/max-min
print("Min-Max scaling for maths scores")
df['Math_Normalized'] = (df['Math']-df['Math'].min()) / (df['Math'].max()-df['Math'].min())
#updated daframe
print(df[['Name' , 'Math','Math_Normalized']])

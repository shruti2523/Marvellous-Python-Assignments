import pandas as pd
import numpy as np

data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[np.nan,76,88],
    'Science':[91,np.nan,85],
}
df = pd.DataFrame(data)
print("Missing Values in Each Column",df.isnull().sum())
import pandas as pd

data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]

}
df = pd.DataFrame(data)
#printing info
print("Information about thev loaded datset is : ")
print("Shape of dataset : ",df.shape)
print("Columns : ",df.columns)
print("Datatypes : ",df.dtypes)


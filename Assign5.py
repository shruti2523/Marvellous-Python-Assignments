import pandas as pd

data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82],
}

df = pd.DataFrame(data)
#printing info
print("Information about thev loaded datset is : ")
print("Shape of dataset : ",df.shape)
print("Columns : ",df.columns)
print("Datatypes : ",df.dtypes)
print("Discriptive Statistics : ",df.describe())

#add column "Total"
df['Total'] = df[['Math','Science','English']].sum(axis=1)
#updated dataframe
print(df)

#Display students get more than 85 marks in science
high_science_scores = df[df['Science']>85]
print("Highest score in Science : ",high_science_scores)

#Replace'pooja' with 'puja'
df['Name'] = df['Name'].replace("Pooja",'Puja')
print(df)

#Sort Total marks in decending order
sorted_df = df.sort_values(by='Total', decending=True)
print(sorted_df)

import pandas as pd
import matplotlib.pyplot as plt

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
print("Replace Pooja with puja")
df['Name'] = df['Name'].replace("Pooja",'Puja')
print(df)

#Sort Total marks in decending order
print("Decending Order")
sorted_df = df.sort_values(by='Total', ascending=False)
print(sorted_df)

#print("Visual Representation")
#plt.figure(figsize = (8,5))  #first size big
#plt.bar(df['Name'],df['Total'],color='blue',label = "Actual")
#plt.xlabel("Student Names")
#plt.ylabel("Total Marks")
#plt.title("Total Marks of Student")
#plt.grid(True)
#plt.show()

print("Line chart")
Amit_marks = df[df['Name'] == 'Amit'][['Math','Science','English']].iloc[0]
plt.figure(figsize = (8,5))  #first size big
plt.plot(Amit_marks.index,Amit_marks.values,color='blue',label = "Actual")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Total Marks of Amit Across All Subjects")
plt.grid(True)
plt.show()


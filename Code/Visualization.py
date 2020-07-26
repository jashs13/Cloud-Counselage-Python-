import pandas as pd
import matplotlib.pyplot as plt

file_name = 'file.csv'
df = pd.read_csv(file_name)
df = df[['Institute code','College Name', 'District']]
print(df.head())

districts = df['District'].tolist()
print(districts)
print("After removing duplicates")
districts = list(dict.fromkeys(districts))
print(districts)

df = df.groupby('District')
Y_axis_num = []

group1 = df.get_group("Mumbai City")
#print(group1)
index = group1.index
number_of_rows = len(index)
print(number_of_rows)
Y_axis_num.append(number_of_rows)

group2 = df.get_group("Mumbai Suburban")
#print(group2)
index = group2.index
number_of_rows = len(index)
print(number_of_rows)
Y_axis_num.append(number_of_rows)

group3 = df.get_group("Ratnagiri")
#print(group3)
index = group3.index
number_of_rows = len(index)
print(number_of_rows)
Y_axis_num.append(number_of_rows)

group4 = df.get_group("Raigad")
#print(group4)
index = group4.index
number_of_rows = len(index)
print(number_of_rows)
Y_axis_num.append(number_of_rows)

group5 = df.get_group("Sindhudurg")
#print(group5)
index = group5.index
number_of_rows = len(index)
print(number_of_rows)
Y_axis_num.append(number_of_rows)

group6 = df.get_group("Thane")
#print(group6)
index = group6.index
number_of_rows = len(index)
print(number_of_rows)
Y_axis_num.append(number_of_rows)

group7 = df.get_group("Palghar")
#print(group7)
index = group7.index
number_of_rows = len(index)
print(number_of_rows)
Y_axis_num.append(number_of_rows)

print(Y_axis_num)

# Visualization
plt.title("Number of colleges per District")
plt.xlabel("District")
plt.ylabel("Number of Colleges")

plt.bar(districts, Y_axis_num)
plt.show()


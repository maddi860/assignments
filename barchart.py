import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#This is how I have included the data into my code
year24=pd.read_csv('year24.csv')
year23=pd.read_csv('year23.csv')
year22=pd.read_csv('year22.csv')


#I have sliced the data so I'm only using the parts that I want in my graphs
year22_data=year22.iloc[:, 1]
year23_data=year23.iloc[:, 1]
year24_data=year24.iloc[:, 1]
months=np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
                 'Oct', 'Nov', 'Dec'])


#This is the code for my first graph
plt.subplot(2, 2, 1)
plt.bar(months, year22_data, width= 0.6, color= 'blue')
plt.xlabel('Months')
plt.ylabel('Number of Days it Rains')
plt.title('Year 2022')


#This is the code for my second graph
plt.subplot(2, 2, 2)
plt.bar(months, year23_data, width= 0.6, color= 'red')
plt.xlabel('Months')
plt.ylabel('Number of Days it Rains')
plt.title('Year 2023')

#This is the code for the third graph
plt.subplot(2, 2, 3)
plt.bar(months, year24_data, width= 0.6, color= 'green')
plt.xlabel('Months')
plt.ylabel('Number of Days it Rains')
plt.title('Year 2024')


#Adjusting the spacing between the sub graphs so the writting can be seen
plt.subplots_adjust(wspace= 0.4, hspace= 0.5)
plt.savefig('barchart')
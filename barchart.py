import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


year24=pd.read_csv('year24.csv')
year23=pd.read_csv('year23.csv')
year22=pd.read_csv('year22.csv')


year22_data=year22.iloc[:, 1]
year23_data=year23.iloc[:, 1]
year24_data=year24.iloc[:, 1]
months=np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
                 'Oct', 'Nov', 'Dec'])


plt.subplot(2, 2, 1)
plt.bar(months, year22_data, width= 0.6, color= 'blue')
plt.xlabel('Months')
plt.ylabel('Number of Days it Rains')
plt.title('Year 2022')


plt.subplot(2, 2, 2)
plt.bar(months, year23_data, width= 0.6, color= 'red')
plt.xlabel('Months')
plt.ylabel('Number of Days it Rains')
plt.title('Year 2023')


plt.subplot(2, 2, 3)
plt.bar(months, year24_data, width= 0.6, color= 'green')
plt.xlabel('Months')
plt.ylabel('Number of Days it Rains')
plt.title('Year 2024')


plt.subplots_adjust(wspace= 0.4, hspace= 0.5)
plt.savefig('barchart')
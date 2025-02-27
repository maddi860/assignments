import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib auto


year24=pd.read_csv('year24.csv')
year23=pd.read_csv('year23.csv')
year22=pd.read_csv('year22.csv')


year22_data=year22.iloc[:, 1]
year23_data=year23.iloc[:, 1]
year24_data=year24.iloc[:, 1]
data=(year22_data+year23_data+year24_data)
labels=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
                 'Oct', 'Nov', 'Dec')


plt.pie(data, labels=labels, startangle= 90, autopct= '%1.1f%%')
plt.title('Total days of rain for 2022-2024')


plt.show()
plt.savefig('piechart')


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
t=np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
                 'Oct', 'Nov', 'Dec'])

plt.figure()


#Here i have plotted the graphs
#I have used alpha to make the lines more transparent so all the lines can be seen clearly
plt.plot(t, year22_data, color= 'blue', label= '2022', alpha= 0.8)
plt.plot(t, year23_data, color= 'red', label= '2023', alpha= 0.8)
plt.plot(t, year24_data, color= 'purple', label= '2024')


#These are the customizations to the graph
plt.xlabel('Months')
plt.ylabel('Number of Days')
plt.title('Number of days of rain 2022-2024')
plt.legend()
plt.grid()


plt.show()
plt.savefig('Lineplot')

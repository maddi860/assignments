import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

year24=pd.read_csv('year24.csv')
year23=pd.read_csv('year23.csv')
year22=pd.read_csv('year22.csv')

year22_data=year22.iloc[:, 1]
year23_data=year23.iloc[:, 1]
year24_data=year24.iloc[:, 1]
t=np.linspace(0, len(year22_data)-1, len(year22_data))

plt.figure()
plt.plot(t, year22_data, color='blue', label='2022', alpha=0.8)
plt.plot(t,year23_data, color='red', label='2023', alpha=0.8)
plt.plot(t,year24_data, color='purple', label='2024')
plt.xlim(-1, 13)
plt.ylim(6, 22)
plt.xlabel('Months')
plt.ylabel('Number of Days')
plt.title('Number of days of rain 2022-2024')
plt.legend()
plt.grid()
plt.show()
plt.savefig('Lineplot')

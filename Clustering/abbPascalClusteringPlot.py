# Imports
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import abbPascalClusteringData as apcd

# load data
apcd.abbPascalClusteringData()

# Sorgt für die Farb Spiele :)
ax = plt.subplot()
ax.set_prop_cycle('color',plt.cm.Spectral(np.linspace(0,1,17)))

# labels 
plt.xlabel('Time')
plt.ylabel('Error`s')

# plot Data Ist noch Fehler bei der Erzeugung enthalten
plt.scatter(apcd.x10000, apcd.y10000, label='10000 Error`s')
plt.scatter(apcd.x11000, apcd.y11000, label='11000 Error`s')
plt.scatter(apcd.x20000, apcd.y20000, label='20000 Error`s')
plt.scatter(apcd.x32000, apcd.y32000, label='32000 Error`s')
plt.scatter(apcd.x34000, apcd.y34000, label='34000 Error`s')
plt.scatter(apcd.x37000, apcd.y37000, label='37000 Error`s')
plt.scatter(apcd.x38000, apcd.y38000, label='38000 Error`s')
plt.scatter(apcd.x39000, apcd.y39000, label='39000 Error`s')
plt.scatter(apcd.x40000, apcd.y40000, label='40000 Error`s')
plt.scatter(apcd.x41000, apcd.y41000, label='41000 Error`s')
plt.scatter(apcd.x50000, apcd.y50000, label='50000 Error`s')
plt.scatter(apcd.x71000, apcd.y71000, label='71000 Error`s')
plt.scatter(apcd.x80000, apcd.y80000, label='80000 Error`s')
plt.scatter(apcd.x100000, apcd.y100000, label='100000 Error`s')
plt.scatter(apcd.x110000, apcd.y110000, label='110000 Error`s')
plt.scatter(apcd.x130000, apcd.y130000, label='130000 Error`s')

# beautify the x-labels
plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter('%Y-%m-%d %H:%M:%S')
plt.gca().xaxis

plt.legend(loc='best')

plt.show()
plt.close()
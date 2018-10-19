# Imports
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd


#Daten einlesen
data = pd.read_pickle("D:/Eclipse Python/DataScience/res/event_ano.pkl");

#Daten in neue Variable schreiben
data1 = data

del data1['an_title']
del data1['an_description']
del data1['message_category']
del data1['message_severity']
del data1['an_line']
del data1['an_cell']

# data
timeStamp = data1[data1.columns[0]].values
x = []
y = [int(numeric_string) for numeric_string in data1[data1.columns[1]].values]

# make up some data
for i in timeStamp:
    dateTime = pd.Timestamp(np.datetime64(i)).to_pydatetime()
    x.append(dateTime)

# Plotten der Bearbeiten Daten im einem Koordinatensystem
plt.xlabel('Time')
plt.ylabel('Error`s')
plt.plot([],[])
plt.scatter(x,y)


# beautify the x-labels
plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter('%Y-%m-%d %H:%M:%S')
plt.gca().xaxis

plt.show()
plt.close()
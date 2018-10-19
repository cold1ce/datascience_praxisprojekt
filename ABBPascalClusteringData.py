# Import
import time
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import MiniBatchKMeans, KMeans
from sklearn.metrics.pairwise import pairwise_distances_argmin
from sklearn.datasets.samples_generator import make_blobs

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

# make up some data
for i in timeStamp:
    dateTime = pd.Timestamp(np.datetime64(i)).to_pydatetime()
    x.append(dateTime)

y = [int(numericString) for numericString in data1[data1.columns[1]].values]

# Aufteilung der Datensätze in Entsprechende Gruppen
x10000 = []
y10000 = []

for i in y:
    if i <= 11000:
        x10000.append(x[i])
        y10000.append(i)

x11000 = []
y11000 = []

for i in y:
    if i >= 11000 and i <= 12000:
        x11000.append(x[i])
        y11000.append(i)

x20000 = []
y20000 = []

for i in y:
    if i >= 20000 and i <= 30000:
        x20000.append(x[i])
        y20000.append(i) 
        
x32000 = []
y32000 = []

for i in y:
    if i >= 32000 and i <= 37000:
        x32000.append(x[i])
        y32000.append(i) 
        
x34000 = []
y34000 = []

for i in y:
    if i >= 34000 and i <= 37000:
        x34000.append(x[i])
        y34000.append(i)     
        
x37000 = []
y37000 = []

for i in y:
    if i >= 37000 and i <= 38000:
        x37000.append(x[i])
        y37000.append(i)  
        
x38000 = []
y38000 = []

for i in y:
    if i >= 38000 and i <= 39000:
        x38000.append(x[i])
        y38000.append(i)    
        
x39000 = []
y39000 = []

for i in y:
    if i >= 39000 and i <= 40000:
        x39000.append(x[i])
        y39000.append(i)
        
x40000 = []
y40000 = []

for i in y:
    if i >= 40000 and i <= 41000:
        x40000.append(x[i])
        y40000.append(i) 
        
x41000 = []
y41000 = []

for i in y:
    if i >= 41000 and i <= 50000:
        x41000.append(x[i])
        y41000.append(i) 
        
x50000 = []
y50000 = []

for i in y:
    if i >= 50000 and i <= 71000:
        x50000.append(x[i])
        y50000.append(i)
        
x71000 = []
y71000 = []

for i in y:
    if i >= 71000 and i <= 80000:
        x71000.append(x[i])
        y71000.append(i)
        
x80000 = []
y80000 = []

for i in y:
    if i >= 80000 and i <= 100000:
        x80000.append(x[i])
        y80000.append(i)
        
x100000 = []
y100000 = []

for i in y:
    if i >= 100000 and i <= 110000:
        x100000.append(x[i])
        y100000.append(i)
        
x110000 = []
y110000 = []

for i in y:
    if i >= 110000 and i <= 130000:
        x110000.append(x[i])
        y110000.append(i) 
        
x130000 = []
y130000 = []

for i in y:
    if i >= 130000:
        x130000.append(x[i])
        y130000.append(i) 
        

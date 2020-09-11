import sqlite3, time, datetime
import csv
import json 
import numpy as np 
import matplotlib.pyplot as plt 

conn = sqlite3.connect("sensehat.db")
cursor = conn.cursor()
sql = "select * from temp_humid;"
cursor.execute(sql)
result = cursor.fetchall()
temp=[]
humid=[]
datetime=[]
for tuple in result:
    temp.append(tuple[1])
    humid.append(tuple[2])
    date=tuple[3]
    dates=int(date[8:10])
    datetime.append(dates)
    
    print(temp)

fig = plt.figure()
plt.plot(temp)
plt.plot(humid)
plt.xlabel('x-Axis')
plt.ylabel('Temperature and Humidity ')
plt.title('Temperature & Humidity Reading')

plt.show()
fig.savefig('Temperature_Humidity.png')
conn.close()
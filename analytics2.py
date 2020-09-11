import csv
import leather
import sqlite3 

conn = sqlite3.connect("sensehat.db")
cursor = conn.cursor()
sql = "select * from temp_humid;"
cursor.execute(sql)
result = cursor.fetchall()
temp=[]
humid=[]

j=0
for record in result:
    t = record[1]
    h = record[2]
    temp.append((j,t))
    humid.append((j,h))
    j+=1
    
chart = leather.Chart('Temperature and Humidity Reading')
chart.add_line(temp)
chart.add_line(humid)
chart.to_svg('temperature_humid_reading2.svg')
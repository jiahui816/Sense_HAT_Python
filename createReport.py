import sqlite3
import csv
import time
import json 


conn = sqlite3.connect("sensehat.db")
cursor = conn.cursor()
sql = "select * from temp_humid;"
cursor.execute(sql)
result = cursor.fetchall()
for tuple in result:
    temp = tuple[1]
    humid = tuple[2]
    print('temp:' + str(temp) + 'humid:' + str(humid))


head=['localTime','data']
cursor.execute(sql)
with open('config.json','r') as comparison:
    value_list = json.load(comparison)
    min_temp = value_list['min_temperature']
    max_temp = value_list['max_temperature']
    min_humid = value_list['min_humidity']
    max_humid = value_list['max_humidity']
#result <> min max//////
if temp > min_temp and temp < max_temp and humid > min_humid and humid < max_humid:
    message = "STATUS: OK"
elif temp < min_temp and humid < min_humid:
    message = "STATUS: BAD. Temperature and Humidity Lower Than Usual"
elif temp > max_temp and humid > max_humid:
    message = "STATUS: BAD. Temperature and Humidity Higher Than Usual"
elif humid < min_humid:
    message = "STATUS: BAD. HUMID TOO LOW"
elif humid > max_humid:
    message = "STATUS: BAD. HUMID TOO HIGH"
elif temp < min_temp:
    message = "STATUS: BAD. TEMP TOO LOW"
elif temp > max_temp:
    message = "STATUS: BAD. TEMP TOO HIGH"
else:
    "ERROR"

#send
with open("report.csv","a") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(head)
    for row in cursor:
        timeDate= time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        writer.writerow([timeDate, row, message])


    
conn.close()


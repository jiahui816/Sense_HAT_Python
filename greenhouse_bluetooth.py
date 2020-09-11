import time
import sqlite3
from sense_hat import SenseHat

sense = SenseHat()

temperature = round(sense.get_temperature(), 1)
pressure = round(sense.get_pressure(), 1)
humidity = round(sense.get_humidity(), 1)
timeDate= time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

connection = sqlite3.connect('sensehat.db')
cursor = connection.cursor()
cursor.execute ('create table if not exists temp_humid(ID integer primary key,temp real,humid real, datetime text);')
cursor.execute("insert into temp_humid values(null,?,?,?);",(temperature,humidity,timeDate))
connection.commit()


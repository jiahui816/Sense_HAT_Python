import time
import sqlite3
from sense_hat import SenseHat
dbname='sensehat.db'
sampleFreq = 1

#get data from SenseHat sensor
def get_temperature():
    sense = SenseHat()
    temp = sense.get_temperature()
    
    return temp
        
# log sensor data on database
def log_temperature (temp):
        conn=sqlite3.connect(dbname)
        curs=conn.cursor()
        curs.execute("INSERT INTO SENSEHAT_data values(datetime('now'),(?));", (temp,))
        conn.commit()

#get data from SenseHat sensor
def get_humidity():
    sense = SenseHat()
    humidity = sense.get_humidity()
    
    return humidity

# log sensor data on database
def log_humidity (humidity):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO SENSEHAT_data values(datetime('now'),(?));", (humidity,))
    conn.commit()


    # display database data
def displayData():
        conn=sqlite3.connect(dbname)
        curs=conn.cursor()
        print ("\nEntire database contents:\n")
        for row in curs.execute("SELECT * FROM SenseHat_data"):
            print (row)
        
        
    # main function
def main():
        for i in range (0,3):
            log_temperature(get_temperature())
            log_humidity(get_humidity())
            time.sleep(sampleFreq)
        displayData()
        
main()
displayData()
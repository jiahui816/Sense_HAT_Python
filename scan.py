import bluetooth
import time

class scan:
    def scanBt():
        myMAC = 'FC:2A:9C:86:13:F9'

        print("Scanning...")
        nearbyDevices = bluetooth.discover_devices()
        if(len(nearbyDevices) == 0):
            print('nothing find')

        for macAddress in nearbyDevices:
            print(macAddress)
            if macAddress.find(myMAC)!=-1:
                print('true')
                return True
            else:
                print('false')
                return False
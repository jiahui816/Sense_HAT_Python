import requests
import json
import os
from sense_hat import SenseHat

ACCESS_TOKEN="o.Mkrx7RINwwbBkm08A8JdVn4bYFwnV3cf"

def send_notification_via_pushbullet():
        """ Sending notification via pushbullet.
            Args:
                title (str) : title of text.
                body (str) : Body of text.
        """
        jinglai = ''
        sense = SenseHat()
        t =sense.get_temperature()
        h =sense.get_humidity()
        body = "Hello outside environment information are: temperature: " + str(t)+ "  Humidity: "+str(h)
        data_send = {"type": "note", "title": jinglai, "body": body}
        resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                            headers={'Authorization': 'Bearer ' + ACCESS_TOKEN,
                            'Content-Type': 'application/json'})
        if resp.status_code != 200:
            raise Exception('Something wrong')
        else:
            print('complete sending')
        
#main function
def main():
        ip_address = os.popen('hostname -I').read()
        send_notification_via_pushbullet()

#Ececute
main()
    
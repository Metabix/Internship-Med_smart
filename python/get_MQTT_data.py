import paho.mqtt.client as mqtt
import sys
import time
import json

MQTT_ADDRESS = '192.168.43.63'
MQTT_USER = 'esppi'
MQTT_PASSWORD = 'esppi'
MQTT_TOPIC = 'home/+/+'


def on_connect(client, userdata, flags, rc):
    """ The callback for when the client receives a CONNACK response from the server."""
    #print('Connected with result code ' + str(rc))
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    """The callback for when a PUBLISH message is received from the server."""
    #print(msg.topic + ' ' + str(msg.payload))
    a = msg.payload
    #print(str(msg.payload))
    b = a.decode('utf-8')
    print(str(b))
    sys.stdout.flush()
    data = {"temperature": b}
    with open("js/temperature.json", "w") as write_file:
        json.dump(data, write_file)

    
def main():
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message
    #print("trouble shoot12",on_message)

    mqtt_client.connect(MQTT_ADDRESS, 1883)
    #mqtt_client.loop_start()
    mqtt_client.loop_forever()
    
    #time.sleep(12)
    #exec(open('bcode.py').read())
    #mqtt_client.loop_stop()
    #exit()

if __name__ == '__main__':
    #print('MQTT to InfluxDB bridge')
    main()
 



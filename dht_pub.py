import paho.mqtt.client as mqtt
import json
import time
import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
pin = 4


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)


client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish
client.connect('localhost', 1883)
client.loop_start()
while True:
    h, t = Adafruit_DHT.read_retry(sensor, pin)
    if h is not None and t is not None :
        print("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%".format(t, h))
        client.publish('Lee', h,1)
        client.publish('common', t,1)
    else :
        print('Read error')
    time.sleep(2)
client.loop_stop()
client.disconnect()
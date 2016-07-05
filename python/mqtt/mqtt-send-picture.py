import paho.mqtt.client as mqtt
import numpy as np
import time

import cv2

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("file")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    buf = msg.payload
    nparr = np.fromstring(buf, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite("test.jpg", img)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.vetrm.net", 1883, 60)

client.loop_start()

cv2.namedWindow("pic")
cap = cv2.VideoCapture(0)

while True:
    print("* recording")
    sound_buf = b'asdfasdf'

    _, img = cap.read()
    ret, buf = cv2.imencode(".jpg", img)

    print("* send")
    client.publish("file", buf.tostring())

    time.sleep(5)

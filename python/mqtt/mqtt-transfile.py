import paho.mqtt.client as mqtt
import time

FILE_DUP_NAME = __file__ + ".copy"
FILE_ORI_NAME = __file__

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("file")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    with open(FILE_DUP_NAME, "wb") as f:
        f.write(str(msg.payload))
        print(msg.topic+" got message")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.vetrm.net", 1883, 60)

client.loop_start()

while True:
    time.sleep(1)
    with open(FILE_ORI_NAME, "rb") as f:
        client.publish("file", bytearray(f.read()))

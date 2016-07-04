import paho.mqtt.client as mqtt
import time

WAVE_DUP_NAME = "test-dup.wav"
WAVE_ORI_NAME = "test-ori.wav"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("file")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    with open(WAVE_DUP_NAME, "wb") as wav:
        wav.write(str(msg.payload))
        print(msg.topic+" got message")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.vetrm.net", 1883, 60)

client.loop_start()

while True:
    time.sleep(1)
    with open(WAVE_ORI_NAME, "rb") as wav:
        client.publish("file", bytearray(wav.read()))

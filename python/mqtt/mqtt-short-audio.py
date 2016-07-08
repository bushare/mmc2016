import paho.mqtt.client as mqtt
import pyaudio
import time

## audio setup
CHUNK = 256
WIDTH = 1
CHANNELS = 1
RATE = 8000
RECORD_SECONDS = 4

pa = pyaudio.PyAudio()

istream = pa.open(format=pa.get_format_from_width(WIDTH),
                  channels=CHANNELS,
                  rate=RATE,
                  input=True,
                  output=False,
                  frames_per_buffer=CHUNK)

ostream = pa.open(format=pa.get_format_from_width(WIDTH),
                  channels=CHANNELS,
                  rate=RATE,
                  input=False,
                  output=True,
                  frames_per_buffer=CHUNK)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("file")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    sound_buf = msg.payload
    ostream.start_stream()
    for idx in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        ostream.write(sound_buf[(idx * WIDTH * CHUNK): ((idx + 1) * WIDTH * CHUNK)],
                      CHUNK)
    ostream.stop_stream()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.vetrm.net", 1883, 60)

client.loop_start()

while True:
    print("* recording")
    sound_buf = bytearray()
    istream.start_stream()
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = istream.read(CHUNK)
        sound_buf += data
    istream.stop_stream()
    print("* done")

    time.sleep(1)

    print("* send")
    client.publish("file", sound_buf)

    time.sleep(5)

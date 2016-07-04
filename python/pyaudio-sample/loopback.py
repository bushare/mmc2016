import pyaudio
import sys

CHUNK = 16
WIDTH = 2
CHANNELS = 1
RATE = 8000
RECORD_SECONDS = 5

pa = pyaudio.PyAudio()

stream = None
if sys.platform == 'win32':
    stream = pa.open(input_device_index=0,
                     output_device_index=2,
                     format=pa.get_format_from_width(WIDTH),
                     channels=CHANNELS,
                     rate=RATE,
                     input=True,
                     output=True,
                     frames_per_buffer=CHUNK)
else:
    stream = pa.open(format=pa.get_format_from_width(WIDTH),
                     channels=CHANNELS,
                     rate=RATE,
                     input=True,
                     output=True,
                     frames_per_buffer=CHUNK)

print("* recording")

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    stream.write(data, CHUNK)

print("* done")

stream.stop_stream()
stream.close()

pa.terminate()

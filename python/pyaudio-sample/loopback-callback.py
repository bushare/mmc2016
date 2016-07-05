import pyaudio
import time

WIDTH = 2
CHANNELS = 1
RATE = 16000
CHUNK = 256

p = pyaudio.PyAudio()


def callback(in_data, frame_count, time_info, status):
    print(frame_count, time_info, status)
    # return None, pa.paComplete when This was the last block of audio data
    return in_data, pyaudio.paContinue

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK,
                stream_callback=callback)

stream.start_stream()

while stream.is_active():
    time.sleep(0.1)

stream.stop_stream()
stream.close()

p.terminate()

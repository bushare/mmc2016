import socket
import struct

import pyaudio

from config import AudioConf as ac
from config import NetConf as nc

pa = pyaudio.PyAudio()
stream = pa.open(format=pa.get_format_from_width(ac.WIDTH),
                 channels=ac.CHANNELS,
                 rate=ac.RATE,
                 input=True,
                 start=False,
                 frames_per_buffer=ac.CHUNK)

multicast_addr = nc.ADDR
port = nc.PORT
bind_addr = '0.0.0.0'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

stream.start_stream()
for idx in range(0, int(ac.RATE / ac.CHUNK * ac.RECORD_SECONDS)):
    data = stream.read(ac.CHUNK)
    sock.sendto(data, (multicast_addr, port))
stream.stop_stream()

sock.close()

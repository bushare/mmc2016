import socket
import pyaudio

from config import AudioConf as ac
from config import NetConf as nc

pa = pyaudio.PyAudio()
stream = pa.open(format=pa.get_format_from_width(ac.WIDTH),
                 channels=ac.CHANNELS,
                 rate=ac.RATE,
                 output=True,
                 start=False,
                 frames_per_buffer=ac.CHUNK)

multicast_addr = nc.ADDR
port = nc.PORT
bind_addr = '0.0.0.0'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
membership = socket.inet_aton(multicast_addr) + socket.inet_aton(bind_addr)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, membership)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((bind_addr, port))

stream.start_stream()
while True:
    data, address = sock.recvfrom(ac.CHUNK)
    stream.write(data)
    print(data, address)
stream.stop_stream()

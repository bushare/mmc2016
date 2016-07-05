## Basic publish/subscribe

```bash
pip install paho-mqtt
```

just do 

```
python mqtt-subscribe.py
```

in one cmd/terminal, and

```
python mqtt-publish.py
```

in another cmd/terminal, you should see some incomming message

## Advanced message like voice and picture

### file

```
python mqtt-transfile.py
```

#### for voice

checkout pyaudio-samples folder and make sure audio has been setup correctly.

run

```
python mqtt-short-audio.py
```

#### pictures

install opencv and python-opencv

```
python mqtt-send-picture.py
```


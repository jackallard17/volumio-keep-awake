#!/usr/bin/env python
import os
import time
import json
from types import SimpleNamespace

run = False

def checkVolumioStatus():
    global run

    status = os.popen('volumio status').read()
    statusJSON = json.loads(status, object_hook=lambda d: SimpleNamespace(**d))
    print(statusJSON.status)

    if statusJSON.status == 'stop':
        run = True
    elif statusJSON.status == 'play':
        run = False
        
#play silent .wav on 15min loop if volumio status is 'stop'
while True:
    checkVolumioStatus()
    print('run: ' + str(run))

    if run:
     os.system('aplay --device=plughw:b1,0 /volumio/app/silence.wav')
     time.sleep(900)
    
    time.sleep(10)
import os
import eel
import subprocess
from engine.feature import *
from engine.command import *
from engine.auth import recoganize

def start():
    eel.init("Frontend")

    playAssistantSound()

    @eel.expose
    def init():
        subprocess.call([r'device.bat'])
        eel.hideLoader()
        speak("Ready for Face Authentication")
        flag = recoganize.AuthenticateFace()
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome Sir, How can I help you")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Face Authentication Failed")

    # Use the same port in both lines
    os.system('start msedge.exe --app="http://localhost:5500/index.html"')

    eel.start('index.html', mode=None, host='localhost', port=5500, block=True)

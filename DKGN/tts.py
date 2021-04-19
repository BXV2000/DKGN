<<<<<<< HEAD
#import cac module can thiet
import speech_recognition as sr
from gtts import gTTS
import os 
import time
import playsound

#tao class tts
class texttospeech:

    #dinh nghia module tts
    def speak(text):
        tts = gTTS(text=text,lang='vi')
        filename = 'voice.mp3'
        tts.save(filename)
        playsound.playsound(filename)


=======
>>>>>>> 426c20a6034c9b75f58b51e0e3eebef812e4d2a1


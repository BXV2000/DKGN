#dieu khien giong noi
import stt
import tts
a=stt.speechtotext
b=tts.texttospeech
b.speak(a.listen())

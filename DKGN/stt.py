#import thu vien nhan dang giong noi
import speech_recognition as sr 

#thiet lap bo phan nhan dien
r = sr.Recognizer()

with sr.Microphone() as source:
    #nhan am thanh tu microphone co san
    print("Vui long noi vao micro...")
    audio_data = r.record(source, duration = 2)
    #chuyen am thanh thanh van ban
    try:
        text = r.recognize_google(audio_data,language="vi") #dinh dang ngon ngu tieng viet
    except:
        text = "Khong the nghe ro loi" #bao loi khi khong nhan duoc am thanh
    print(text)
    

    
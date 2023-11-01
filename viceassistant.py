import pyttsx3 #ye hamare text ko speach me convert karne ke kam karega 
import speech_recognition as sr #speech_recognition ham jo bhi bolenge usko text me convert karega
import webbrowser #ye web broser me kuchh result search karega
import datetime # Isase ham current date time ko nikal sakte hai
from datetime import date# Isase ham current date time ko nikal sakte hai
import pyjokes
import pyttsx3
import os
from PIL import Image
import time

#speak to text function
def speech_text():
    while True:
        recognizer=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listing now......")
            recognizer.adjust_for_ambient_noise(source)
            audio=recognizer.listen(source)
            try:
                print("Recognizing......")
                data=recognizer.recognize_google(audio)
                print(data)
                return data
            except:
                print("not understand ")
            

#text to speach function
def text_speech(x):
    engin=pyttsx3.init()
    voice=engin.getProperty('voices')
    engin.setProperty('voice',voice[0].id)
    speed=engin.getProperty('rate')
    engin.setProperty('rate',120)
    engin.say(x)
    engin.runAndWait()

if __name__=='__main__':
    while True:
        #time.sleep(10)
        data2=speech_text().lower()
        print(data2)
        if "hello ai" in speech_text().lower():
            hello="hello"
            text_speech(hello)
            while True:
                data1=speech_text()
                if "what is your name" in data1.lower():
                    name="my name is hello ai"
                    text_speech(name)
                
                elif "how are you" in data1.lower():
                    name="i am fine"
                    text_speech(name)

                elif "who is anshika" in data1.lower():
                    age="this is a lady"
                    text_speech(age)
                 
                elif "how old are you" in data1:
                    age="i am 23 years old"
                    text_speech(age)
                elif "ok" in data1.lower():
                    age="ok"
                    text_speech(age)
                elif "who is modi" in data1.lower():
                    modi="modi is the prime minister of india"
                    text_speech(modi)
                elif "please tell me current time" in data1.lower():
                    time=datetime.datetime.now().strftime("%I%M%p")# I hour batata hai, M minut batata hai, p pa am and pm batata hai
                    text_speech(time)
                elif "please tell me today date" in data1.lower():
                    
                    today = date.today()
                    # print("Today's date:", today)
                    # time=datetime.datetime.now().strftime("%D")# I hour batata hai, M minut batata hai, p pa am and pm batata hai
                    text_speech(today)
                elif "please open youtube" in data1.lower():
                    webbrowser.open("https://www.youtube.com/")
                elif "song" in data1:
                    webbrowser.open("https://www.youtube.com/watch?v=t67yWypwzXQ&list=RDt67yWypwzXQ&start_radio=1")
                                    
                elif "open image" in data1.lower():
                    # path="C:\Users\Lenovo\Pictures\Screenshots"
                    # listimage=  os.listdir(path)
                    # print(listimage)
                    # os.startfile(os.path.join(path,listimage[0]))
                    image = Image.open("C:/Users/Lenovo/Pictures/Screenshots/Screenshot (45).png")
                    image.show()
                elif "exit" in data1.lower():
                    exit="thank you"
                    text_speech(exit)
                    break
                
                else:
                    text_speech("I don't know")
                
              
        elif "exit" in data2.lower():
            text_speech("thank you") 
            print("exit''''''")     
            break
        else:
            text_speech("please speak hello ai")




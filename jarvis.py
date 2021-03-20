print("Commands of this J.A.R.V.I.S are - \n")

print("# It can greet you when it is morning it will say you morning and when it is afternoon it will say afternoon and otherwise it will say afternoon.\n")
print("# It can listen to your voice and recognize it and then comes to it's output.\n")
print("# It can reply to basic words like hello and fine and when quit it will automatically stop speaking.\n")
print("# It can wikipedia anything.\n")
print("# It can turn on your camera anytime as it has function of security camera.\n")
print("# It can open youtube , amazon , citibank , discord , flipkart , whatsapp , zoom , python , skype , lichess , google.\n")
print("# It can tell you the joke and read it to you also.\n")
print("# It can play any song or any video in youtube.\n")
print("# It can tell you the current time.\n")
print("# It can shutdown automatically.\n")








import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import os
import pyjokes
import cv2
import winsound
import requests



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am jarvis sir What Can I do For You")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


    
 

def SecurityCamera():
    cam = cv2.VideoCapture(0)
    while cam.isOpened():
        ret,frame1 = cam.read()
        ret,frame2 = cam.read()
        diff = cv2.absdiff(frame1 , frame2)
        gray = cv2.cvtColor(diff , cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh , None , iterations=3)
        contours, _ = cv2.findContours(dilated , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(frame1 , contours, -1 , (0 , 255 , 0) , 2)
        for c in contours:
            if cv2.contourArea(c) < 5000:
                continue
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(frame1 , (x , y) , (x + w , y + h) , (0 , 255 , 0) , 2)
            winsound.Beep(500,100)
        if cv2.waitKey(10) == ord('q'):
            break
        cv2.imshow('Dakshit cam' , frame1)


if __name__ == "__main__":
    wish()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        
            

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'hello' in query:
            speak("Hello sir How are you ")

        elif 'fine' in query:
            speak("that great sir please tell me what can I do")

          

        elif 'play' in query:
            whatShouldPlay = query.replace('play', '')
            speak('playing ' + whatShouldPlay)
            pywhatkit.playonyt(whatShouldPlay)


         

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'quit' in query:
            speak("Bye Sir Have A Nice Day.")
            speak("If You Want More Help Please call Me Again.")
            speak("Thank You Sir")
            exit()

        elif 'camera' in query:
            SecurityCamera()

        elif 'open amazon' in query:
            webbrowser.open("https://www.amazon.in/")

        elif 'open citibank' in query:
            webbrowser.open(".citibank.co.in/ibank/login/IQPin1.jsp?dOfferCode=PAYCCBILL")

        elif 'open discord' in query:
            webbrowser.open("https://discord.com/channels/777879401990717470/777879401990717473")

        elif 'open whatsapp' in query :
            codePath = "https://web.whatsapp.com/"
            os.startfile(codePath)

        elif 'open zoom' in query :
            codePath = "https://zoom.us/"
            os.startfile(codePath)

        elif 'open python' in query :
            codePath = "https://www.python.org/"
            os.startfile(codePath)
        elif 'open skype' in query :
            codePath = "https://www.skype.com/en/"
            os.startfile(codePath)

        elif 'open lichess' in query :
            codePath = "https://lichess.org/"
            os.startfile(codePath)

        elif 'open google' in query :
            codePath = "https://www.google.com/"
            os.startfile(codePath)

        elif 'open flipkart' in query :
            codePath = "https://www.flipkart.com/"
            os.startfile(codePath)

        elif 'shutdown' in query:
            speak("Do you really want to shutdown your sysytem sir ?")
            relpy = takeCommand().lower()
            if 'yes' in relpy:
                os.system('shutdown /s /t 1')
            else:
                speak("As you wish sir ! ")

          
                
                
            
             
    

         

         


            

        

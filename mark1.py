import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import platform

global state
state=True


#we calling windows API for voice reconginition
engine=pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voice)
engine.setProperty('voice', voice[0].id)
engine.setProperty('rate', 150)
# print(voice[0].id)

#speaking 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#greeting
def greet():
    hourr=int(datetime.datetime.now().hour)
    if hourr<12:
        msg='Good Morning Sir!'
    elif hourr>12:
        msg='Good Afternoon Sir!'
    speak(msg)
    speak('I am Robo Your first Artificial Intelligence')
    speak('How I can help you')

#take commands
def takecommand():
    query=input('Enter your queries').lower()
    strr=''
    # r=sr.Recognizer()
    # with sr.Microphone() as source: 
    #     recording.adjust_for_ambient_noise(source)
    #     print("Listening.......:")
    #     audio = r.listen(source)
    
    if 'time' in query:
        x=datetime.datetime.now()
        timee=x.strftime("%X")
        speak(timee)
    if 'date' in query:
        x=datetime.datetime.now()
        timee=x.strftime("%d %B %Y")
        speak(timee)
        
    if query=='quit':
        global state
        speak('Shutdown initiated')
        state=False

    if 'wikipedia' in query:
        query=query.replace('wikipedia','')
        speak('Searching initiated......')
        try:
            msg=wikipedia.summary(query,sentences=2)
            speak(msg)
        except Exception as e:
            speak('Nothing found')
            takecommand()

    if 'search ' in query:
        query=query.replace('search ','')
        url='https://'+query
        speak('Granting Access to Webbrowser')
        try:
            webbrowser.open(url)
        except Exception as e:
            speak('Url not found')

    if query=='open google':
        speak('Granting access')
        webbrowser.open('https://www.google.com')

    if 'run' in query:
        query=query.replace('run','')

    if 'joke' in query:
        jokes=pyjokes.get_joke(language='en',category='neutral')
        speak(jokes)
    
    if 'system information' in query:
        info=f'''Operating system {platform.system()}
        Processor {platform.processor()}
        System version {platform.version()}
        '''
        speak(info)

        
    
if __name__=='__main__':
    greet()
    while state==True:
        takecommand()
    
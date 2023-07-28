import speech_recognition as sr
import pyttsx3
import pywhatkit                           #powerful package to search youtube
import datetime                            # package to get date,time
import wikipedia
import pyjokes


listerner=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')          #for changing voice
engine.setProperty('voice',voices[1].id)      #female voice

engine.say('I am your alexa')            
engine.say('What can I do for you')
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():                    #alexa listening through microphone
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice=listerner.listen(source)
            command=listerner.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)

    except:
        pass
    return command

def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is'+time)

    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,5)
        print(info)
        talk(info)

    elif 'date' in command:
        
        talk('sorry,I am a virtual assistant find someone else')

    elif 'are you single' in command:
        talk("I am in a relationship with wifi")
        print()

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        #print()

    elif 'hello how are you' in command:
        talk('hey! I am doing well, thanks for asking.What about you? ')

    elif 'I am also good' in command:
        talk('Thats great to hear')


    else:
        talk('Please say the command again...')
        


    
while True:         #running in loop
    run_alexa()


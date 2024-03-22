import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
#import threading
#import tkinter as tk
#qimport sys

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#def __init__():
#    root = tk.Tk()
#    label = tk.Label(root, text="😉", font=("Cambria", 270, "bold"))
#    label.pack()
#    root.mainloop()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def open_py_file():
    cmd1 = 'python MyVMGR1.py'
    p = subprocess.Popen(cmd1, shell=True)


def open_MyEC_file():
    cmd2 = 'python MyVMEC.py'
    p = subprocess.Popen(cmd2, shell=True)


def open_SC_file():
    cmd3 = 'python Screen_R.py'
    p = subprocess.Popen(cmd3, shell=True)

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            talk('listening')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                talk(command)
                print(command)
            #print(command)
    except:
        pass
    return command

def run_alexa():
    #__init__()
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        print('Playing' + song + 'on YouTube')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'known college in surat' in command:
        print('Shree Swami Atmanand Saraswati Institute of Technology a.k.a. Ssasit,')
        print('is one of the popular and well known college for engineering in surat. ')
        print('It includes departments like Computer, Mechanical, Civil, EC, Electrical, IT, MScIT, etc. ')
        print('My Creator Mr Mitanshu Belongs to Computer Department.')
        talk('Shree swami Atmanand saraswati institute of Technology a.k.a. Ssasit, is one of the popular and well known college for engineering, in surat. It includes departments like Computer, Mechanical, Civil, EC, Electrical, IT, M S C IT, etcetra. My Creator, Miss Shweta Belongs to Computer Department.')
    elif 'joke' in command:
        thejoke = pyjokes.get_joke()
        print(thejoke)
        talk(thejoke)
    elif 'my virtual mouse' in command:
        open_py_file()
        print('Opening your Virtual Mouse Gesture Recognizer')
        talk('Opening your Virtual Mouse Gesture Recognizer')
    elif 'my E M B C' in command:
        open_MyEC_file()
        print('Opening your Eyes Based Mouse Controller')
        talk('Opening your Eyes Based Mouse Controller')
    elif 'my Screen Recorder' in command:
        open_SC_file()
        print('Opening your own Screen Recorder')
        talk('Opening your own Screen Recorder')
    else:
        talk('Please say the command again.')

while True:
    run_alexa()
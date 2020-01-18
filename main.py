# import packages
import pyttsx3                              # text to speech (https://github.com/nateshmbhat/pyttsx3)
import speech_recognition as sr             # speech recognition (https://github.com/Uberi/speech_recognition)
import datetime                             # access date and time
import wikipedia                            # access wikipedia content from the python program
import webbrowser                           # access web browser
import os
import smtplib



print('Initializing A')

MASTER = 'Ali'

engine = pyttsx3.init()                         # object creation

"""RATE"""
# rate = engine.getProperty('rate')             # getting details of current speaking rate
# print (rate)                                  # printing current voice rate
engine.setProperty('rate', 140)                 # setting up new voice rate
# rate = engine.getProperty('rate')             # getting details of current speaking rate

"""VOICE"""
voices = engine.getProperty('voices')           # getting details of current voice
engine.setProperty('voice', voices[0].id)       # changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)     # changing index, changes voices. 1 for female



"""Function to pronounce any string"""
def speak(text):
    engine.say(text)                            
    engine.runAndWait()

"""Wishing after Initialization"""
def wishMe():
    # import datetime module to insert time
    hour = int(datetime.datetime.now().hour)            # select time (hour)
    minute = datetime.datetime.now().time().minute      # select time (minutes)
    print(f'Time is {hour}:{minute}')

    # conditions for morning, afternoon, evening
    if hour>=0 and hour<12:
        speak('Good Morning' + MASTER)

    elif hour>=12 and hour<18:
        speak('Good Afternoon' + MASTER)

    else:
        speak('Good Evening' + MASTER)

    # speak time (hour and minute)
    speak(f'I am A. The time is {hour} hours and {minute} minutes.')

    # after wishing
    speak('How may I help you?')

"""Function for taking commands from microphone""" 
def takeCommand():
    # https://www.simplifiedpython.net/speech-recognition-python/
    r = sr.Recognizer()                         # recognize voice
    with sr.Microphone() as source:             # source of voice
        print('Listening...')
        audio = r.listen(source)                # listen to the source and store it in the audio

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')     # recognizer to convert audio to text
        print(f'You said {query}\n')

    except:
        print('I didn\'t understand what you said.Can you please repeat.')
        query = None
    
    return query


speak('Initializing A.....')
wishMe()
query = takeCommand()

"""Execution of Wikipedia query"""
if 'wikipedia' in query.lower():                           # search 'Wikipedia' word in query
    speak('Searching Wikipedia.....')                      # if found (speak)
    query = query.replace('Wikipedia', '')                 # remove 'Wikipedia' from query to search only for desired word
    results = wikipedia.summary(query, sentences=2)
    print(results)

elif 'open youtube' in query.lower():
    url = 'youtube.com'
    # Windows path for chrome
    chrome_path = 'C:/Users/HCL/AppData/Local/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'google it' in query.lower():
    speak('Wait for Google results.....')
    query = query.replace('Google it', '')
    url = "http://www.google.com/?#q="
    chrome_path = 'C:/Users/HCL/AppData/Local/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url + query)

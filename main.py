# import packages
import pyttsx3                              # text to speech
import speech_recognition as sr             # speech recognition
import datetime                             
import wikipedia
import webbrowser
import os
import smtplib

print('Initializing Amili')

engine = pyttsx3.init()                     # object creation

"""RATE"""
# rate = engine.getProperty('rate')             # getting details of current speaking rate
# print (rate)                                  # printing current voice rate
engine.setProperty('rate', 140)                 # setting up new voice rate
# rate = engine.getProperty('rate')             # getting details of current speaking rate

"""VOICE"""
voices = engine.getProperty('voices')           #getting details of current voice
engine.setProperty('voice', voices[0].id)       #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)     #changing index, changes voices. 1 for female

"""STRING TO SPEECH"""
def speak(text):                                # define a function
    engine.say(text)                            #   
    engine.runAndWait()

""" """    
def wishMe():
    hour = datetime.datetime.now().hour
    print(hour)

speak('Initializing Amili...')
wishMe()

import wikipedia 
import requests
import pyttsx3
import datetime
import speech_recognition as sr
import os
import smtplib
import psutil
import pyjokes
import pyautogui
import webbrowser as wb
import random
import wolframalpha
import cv2
import numpy as np
from playsound import playsound
from ultralytics import YOLO
import supervision as sv
import torch
import subprocess

# Initialize voice engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
wolframalpha_app_id = "6YKJH2-45J43UPXHV"

# Helper function to speak text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    return audio

# Define assistant functions
def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        return speak("Good Morning!")
    elif 12 <= hour < 18:
        return speak("Good Afternoon!")
    else:
        return speak("Good Evening!")
    speak("I am Angel, how can I help you, sir?")

def search_wikipedia(query):
    result = wikipedia.summary(query, sentences=2)
    return speak(f"According to Wikipedia: {result}")

# Other functions like sendEmail, cpu, joke, screenshot etc. can be added here in a similar way.
# Each function should return a string message to be displayed in the web UI.

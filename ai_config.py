# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:57:35 2021

@author: Junaid Alam
"""
import speech_recognition as sr
import pyttsx3
import datetime
from playsound import playsound
import os
import json

speech_listener = sr.Recognizer()
engine = pyttsx3.init()

surahs = json.loads(open("surahs.json").read())
default_audio_directory = "\\recitation\\"
current_directory = os.getcwd()
audio_directory = current_directory + default_audio_directory
voices = engine.getProperty('voices')
MALE_VOICE = voices[0].id
FEMALE_VOICE = voices[1].id

# todo : all these values to be made customizable in future version
engine.setProperty('voice', FEMALE_VOICE)
confirm_message = "reciting chapter, {0}, verse, {1}, of the holy quran"
confirm_message1 = "reciting Surah,al, {0}, of the holy quran"
confirm_message2 = "reciting Surah,al, {0}, of the holy quran translated in {1}"
confirm_message3 = "reciting Surah,al, {0}, of the holy quran from veres {1} t0 verse {2}"
error_message = "please say it again clearly, as i could not understand"
wrong_reference = "sorry. it seems you either quoted wrong chapter or verse reference or your voice was not clear"
greeting_message = "As,salaammuualeiikum... May peace.. blessings.. and the guidance of.. AL-LAH, be upon you"
silence_duration = 2


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as mic:
            speech_listener.adjust_for_ambient_noise(mic, silence_duration)
            print('I am ready to accept your command..')
            voice = speech_listener.listen(mic)
            command = speech_listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except sr.UnknownValueError:
        command = error_message
        pass
    return command


def run_ai():
    command = take_command()
    tokens = command.split(" ")
    print(tokens)
    try:
        if 'chapter' in command and 'verse' in command and (len(tokens) >= 4):
            chapter = format_chapter_verse(tokens[1])
            verse = format_chapter_verse(tokens[3])
            talk(confirm_message.format(tokens[1], tokens[3]))
            file = chapter + verse
            recite(file)
        elif ('surah' in command or 'sura' in command) and (len(tokens) >= 3):
            if ('translate' in command) and (len(tokens) >= 6):
                talk(confirm_message2.format(tokens[3], tokens[5]))
                recite_translated(tokens[3], tokens[5])
            elif ('verse' in command) and (len(tokens) >= 6):
                print("Verse :")
                talk(confirm_message3.format(tokens[2], tokens[4], tokens[6]))
                recite_surah(tokens[2], int(tokens[4]), int(tokens[6]))

            else:
                talk(confirm_message1.format(tokens[len(tokens) - 1]))
                recite_surah(tokens[len(tokens) - 1])
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        else:
            talk(error_message)
    except Exception as ex:
        print("Error occured " + str(ex))
        talk("sorry.. an error occured")


def recite(chapter_verse):
    try:
        playsound(audio_directory + chapter_verse + ".mp3")
    except FileNotFoundError:
        talk(wrong_reference)


def recite_surah(surah_name, start_at=1, stop_at=0):
    try:
        chapter = format_surah(surahs[surah_name][0])
        print("chapter: " + str(chapter))
        till_verse = (surahs[surah_name][1] + 1) if stop_at == 0 else stop_at + 1
        for i in range(start_at, till_verse):
            verse = format_surah(i)
            chapter_verse = str(chapter) + verse
            print("Surah file " + chapter_verse)
            playsound(audio_directory + chapter_verse + ".mp3")
    except FileNotFoundError:
        talk(wrong_reference)


def recite_translated(surah, language):
    try:
        chapter = surah + "_" + language
        playsound(audio_directory + chapter + ".mp3")
    except FileNotFoundError:
        talk(wrong_reference)


def format_surah(num):
    string = "00" + str(num)
    if (num > 9) and (num < 100):
        string = "0" + str(num)
    elif num > 99:
        string = str(num)
    return string


def format_chapter_verse(token_item):
    string = token_item
    number_of_digits = len(token_item)
    if number_of_digits < 3:
        string = ((3 - number_of_digits) * "0") + token_item

    return string


def greet():
    talk(greeting_message)


# Configuration setters
def set_voice(gender):
    engine.setProperty('voice', voices[gender].id)


# set audio directory
def set_audio_directory(directory):
    global audio_directory
    audio_directory = current_directory + directory


# set the json file for the surahs
def get_surahs_from(filename):
    global surahs
    surahs = open(filename)


# Set silence duration
def set_silence_duration(duration):
    global silence_duration
    silence_duration = duration

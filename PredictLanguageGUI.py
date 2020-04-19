#Date: April 2nd, 2020
#Written by: Oscar Law
#Description: Using machine learning to predict language, first every machine learning project

import pygame
import sys
import string
from Screens import Screen
from PredictLanguageML import counter, classifier
import random

#Initiating pygame
pygame.init()

#Setting caption for program
pygame.display.set_caption("Language Classifier")

#Setting up the screen
screen_width = 1100
screen_height = 650
win = pygame.display.set_mode((screen_width, screen_height))

#Instantiating graphical user interface
gui = Screen(win)

#Setting current text, result and probability of classifying the data and the predicted language
text = ""
result = None
probability = None
predicted_language = None

#Setting up music playlist
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load("PortugueseMusic.mp3")
pygame.mixer.music.play()

#All songs in the playlist
all_songs = ["PortugueseMusic.mp3", "SpanishMusic.mp3", "FrenchMusic.mp3"]

#Plays next song when called
def play_next_song():
    global all_songs
    all_songs = all_songs[1:] + [all_songs[0]]
    pygame.mixer.music.load(all_songs[0])
    pygame.mixer.music.play()

while True:    
    for event in pygame.event.get():
        #Checks if user has exited the screen
        if event.type == pygame.QUIT:
            sys.exit()
        
        #Checks if user has pressed a key
        if event.type == pygame.KEYDOWN:
            #Backspaces text if backspace key is pressed
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            #Classifies data if return key is pressed
            elif event.key == pygame.K_RETURN and text != "":
                text.translate(str.maketrans('', '', string.punctuation))
                new_text = text.lower()
                user_data = counter.transform([new_text])
                result = classifier.predict(user_data)
                probability = classifier.predict_proba(user_data).tolist()
            else:
                #Adds text to the screen if the user has typed less than 120 characters
                if len(text) < 120:
                    text += event.unicode
        
        #Checks if the song has ended
        if event.type == SONG_END:
            play_next_song()

    #Resets current text if the reset button has been pressed or the text is empty
    if gui.button_pressed(150, 430, 300, 100) or text == "":
        text = ""
        result = None
        probability = None
        predicted_language = None

    #Checks if classify button or enter key has been pressed
    if gui.button_pressed(650, 450, 300, 100) and text != "":
        #Transforms data and predicts language based on current text
        text.translate(str.maketrans('', '', string.punctuation))
        new_text = text.lower()
        user_data = counter.transform([new_text])
        result = classifier.predict(user_data)
        probability = classifier.predict_proba(user_data).tolist()

    #Checking if classifer was unable to make a reasonable prediction
    if probability and probability[0].count(probability[0][0]) == len(probability[0]):
        predicted_language = "Insufficient data"    
    #Classifying language based on the results of the classifer
    else:
        if result == [0]:
            predicted_language = "English"
        elif result == [1]:
            predicted_language = "French"
        elif result == [2]:
            predicted_language = "Spanish"
        elif result == [3]:
            predicted_language = "Italian"
        elif result == [4]:
            predicted_language = "Portuguese"
        elif result == [5]:
            predicted_language = "German"
        elif result == [6]:
            predicted_language = "Dutch"
        elif result == [7]:
            predicted_language = "Polish"
        elif result == [8]:
            predicted_language = "Czech"
        elif result == [9]:
            predicted_language = "Romanian"
        elif result == [10]:
            predicted_language = "Norwegian"
        elif result == [11]:
            predicted_language = "Swedish"
        elif result == [12]:
            predicted_language = "Danish"
        elif result == [13]:
            predicted_language = "Finnish"

    #Creates graphical user interface
    gui.create_language_gui(text, predicted_language)

    #Moves text to the next line if current line has 30 characters
    lines = [text[i:i + 30] for i in range(0, len(text), 30)]
    if len(lines) >= 1:
        gui.create_text(40, lines[0], (240, 150))
    if len(lines) >= 2:
        gui.create_text(40, lines[1], (240, 200))
    if len(lines) >= 3:
        gui.create_text(40, lines[2], (240, 250))
    if len(lines) >= 4:
        gui.create_text(40, lines[3], (240, 300))

    pygame.display.update()






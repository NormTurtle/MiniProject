# https://youtu.be/uf8DvQlWm7M  BroCode my believed.

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # hiding the Pygame banner
import time
import datetime
import pygame

# alarm_time = input('Enter Alarm time (MM:SS) ')
alarm_time = '01:20'
sound = 'wake_up.mp3'
pygame.mixer.init()
pygame.mixer.music.load(sound)

def set_alarm(alarm_time):
    print(f'Alarm set for time {alarm_time}')
    running = True
    while running:
        currunt_time = datetime.datetime.now().strftime('%M:%S')
        print(currunt_time,end='\r')
        if alarm_time == currunt_time:
            print('WAKE UP 🗣️')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            running = False
        time.sleep(1)

set_alarm(alarm_time)


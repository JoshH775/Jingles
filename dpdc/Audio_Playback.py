# https://www.pygame.org/docs/ref/music.html
import time


import os
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from tinytag import TinyTag
pygame.init()
global music, sound
music = pygame.mixer.music
sound = pygame.mixer.Sound
MUSIC_END=pygame.USEREVENT+1
music.set_endevent(MUSIC_END)

def playtime(songdir,uptime=0.0):
    if type(songdir)==list:
        songdir=songdir[5]

    currenttime=(music.get_pos()/1000)+(uptime)
    currenttime=time.strftime("%M:%S", time.gmtime(currenttime))
    duration = TinyTag.get(songdir).duration
    songlengthF = time.strftime("%M:%S", time.gmtime(duration))

    times=[currenttime,songlengthF]
    return times
def getPos():
    return music.get_pos()
#music controls
def play(songdir,vol,start=0.0):
    # if type(songdir) == list:
    #     songdir=songdir[0]
    # try:
    #     music.load(songdir)  #trying to load song,checking if .mp3 or .wav
    #     lossless=False
    # except pygame.error:
    #     global currentwav
    #     currentwav=sound(songdir)
    #     lossless=True
    # if lossless==False:
    #     try:
    #         if vol > 1:
    #             vol=0.1
    #         music.set_volume(vol)
    #     except:
    #         music.set_volume(0.1)
    song=songdir[5]

    music.set_volume(vol)
    music.load(song)
    music.play(start=start)
    playtime(song)

def getBusy():
    return music.get_busy()

def setVol(vol):
    music.set_volume(vol)



def pause():
    p = music.get_busy() #returns 0 if not playing, returns 1 if playing

    if p==0:
        music.unpause()

    elif p == 1:
        music.pause()
def endCheck():
    for event in pygame.event.get():
        if event.type==MUSIC_END:
            return True
        else:
            return False



# class PauseControl():
#
#     def __init__(self):
#         self.IsPaused = False
#     def classpause(self):
#         music.pause()
#     def classunpause(self):
#         pygame.mixer.music.unpause()
#     def toggleMusic(self):
#         if self.IsPaused == True:
#             self.classunpause()
#             self.IsPaused = False
#         else:
#             self.classpause()
#             self.IsPaused = True




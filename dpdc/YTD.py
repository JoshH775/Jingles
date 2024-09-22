import PySimpleGUI as sg
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import os, webbrowser, validators, shutil
from mutagen.easyid3 import EasyID3
global mp3



def convertToMp3(filename):
    mp4filename=filename
    mp3filename=filename[:-3]+"mp3"

    audioclip = AudioFileClip(mp4filename) #turning mp4 into videoclip object

    audioclip.write_audiofile(mp3filename) #outputting to mp3 filename
    audioclip.close()
    os.remove(filename)
    return mp3filename


def tags(mp3filename,values,box):

    audio=EasyID3(mp3filename)
    audio["title"]=values["-TITLE-"]
    audio["artist"]=values["-ARTIST-"]
    audio["album"]=values["-ALBUM-"]
    audio["date"]=values["-YEAR-"]
    audio["genre"]=values["-GENRE-"]
    audio.save(v2_version=3)

    sg.Popup("Choose where to save your file, note that you will have to add the folder through the library settings screen.")
    mp3=mp3filename
    dir = filedialog.askdirectory()
    try:
        shutil.move(mp3, dir)
        sg.Popup("Saved!")
        mp3 = mp3.split("\\")
        mp3 = mp3.pop(-1)
        box.close()
        return dir + "/{}".format(mp3)

    except:
        sg.PopupError("An error occured, check if the file with the same name is in the chosen directory")


def download(url):

    ytd = YouTube(url).streams.get_audio_only().download()
    mp3=convertToMp3(ytd)
    return mp3

def main():
    mainlayout=[[sg.Text("Josh's Jingles Youtube Downloader")],
            [sg.Text("Link or Search Query:"),sg.Input(key="-URL-"),sg.Button("Submit",bind_return_key=True)]]
    tageditor=[[sg.Text("Tag Editor",justification="c",font="Calibri 48 bold underline italic")],
               [sg.Text("Title:"),sg.Input(enable_events=True,key="-TITLE-")],
               [sg.Text("Artist:"),sg.Input(enable_events=True,key="-ARTIST-")],
               [sg.Text("Album:"),sg.Input(enable_events=True,key="-ALBUM-")],
               [sg.Text("Year:"),sg.Input(enable_events=True,key="-YEAR-")],
               [sg.Text("Genre:"),sg.Input(enable_events=True,key="-GENRE-"),sg.Button("Submit All",key="-TAGSUBMIT-")]]
    layout=[[sg.Column(mainlayout,visible=True,key="-MAINLAYOUTCOLUMN-"),sg.Column(tageditor,visible=False,key="-TAGEDITORCOLUMN-",element_justification="c")]]
    box=sg.Window(title="Josh's Jingles Youtube Downloader",layout=layout,return_keyboard_events=True)


    while True:
        event, values=box.read()

        if event==sg.WIN_CLOSED:
            box.close()
            break
        if event == "Submit":
            inputvalue=values["-URL-"]
            print(inputvalue)
            box["-URL-"].update("")
            valid=validators.url(inputvalue)
            if valid == True:
                global mp3
                mp3=download(inputvalue)
                print(mp3)
                sg.Popup("Done!")
                box["-MAINLAYOUTCOLUMN-"].update(visible=False)
                box["-TAGEDITORCOLUMN-"].update(visible=True)

            else:
                inputvalue=str(inputvalue)
                inputvalue.replace(" ","+")
                yturl="www.youtube.com/results?search_query="+inputvalue
                webbrowser.open(yturl)
                gurl="https://www.google.com/search?q="+inputvalue
                webbrowser.open(gurl)

        if event == "-TAGSUBMIT-":
            mp3=tags(mp3,values,box)
            return mp3






